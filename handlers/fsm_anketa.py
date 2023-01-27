from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import gender_markup, cancel_markup
from db.base import create_order
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class FSMAdmin(StatesGroup):
    product_id = State()
    name = State()
    age = State()
    gender = State()
    region = State()
    done = State()


async def fsm_start(call: types.CallbackQuery, state: FSMContext):
    await FSMAdmin.product_id.set()
    async with state.proxy() as data:
        data['product_id'] = int(call.data.replace('fsm_start', ''))
    await FSMAdmin.next()
    await call.bot.send_message(chat_id=call.from_user.id,
                                text="Ваше имя?", reply_markup=cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Ваш возраст?")


async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) <= 0:
            await message.answer("Только положительные числа!")
        else:
            if 16 < int(message.text) < 50:
                async with state.proxy() as data:
                    data['age'] = int(message.text)
                await FSMAdmin.next()
                await message.answer("Укажите пол", reply_markup=gender_markup)
            else:
                await message.answer("Доступ воспрещен!")
    except ValueError:
        await message.answer("Числа брат, числа")


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer("Откуда будете?", reply_markup=cancel_markup)


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text

        yes_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        yes_kb.add(
            KeyboardButton('ДА'),
            KeyboardButton('НЕТ')
        )

        await FSMAdmin.next()
        await message.answer(
            f"{data['name']} {data['age']} {data['gender']} "
                    f"{data['region']}\n\n{data['username']} - Все верно?", reply_markup=yes_kb
        )



async def submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        create_order(data)
    await message.answer('мы с вами свяжемся!')



async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")


def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(load_name, Text(equals='НЕТ'), state=FSMAdmin.done)
    dp.register_callback_query_handler(fsm_start, Text(startswith=['fsm_start']))
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    # dp.register_message_handler(load_photo, state=FSMAdmin.photo)
    dp.register_message_handler(submit, Text(equals='ДА'), state=FSMAdmin.done)