from config import bot
from aiogram import Dispatcher, types
from keyboards.client_kb import start_markup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import randint
from handlers.zinzin import s_command
from aiogram.dispatcher.filters import Text
from cars.carrrr import show_cars
async def start_command(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("МЕНЮ", callback_data="button_call_1")
    button_call_2 = InlineKeyboardButton("Адрес", callback_data="button_call_2")
    markup.add(button_call_1, button_call_2)
    await bot.send_message(message.from_user.id,
                           text=f'Привет, {message.from_user.first_name}, я буду вашим собеседником',
                           reply_markup=markup)


async def myinfo(message: types.Message):
    await bot.send_message(message.from_user.id, f'''
id: {message.from_user.id}
first_name: {message.from_user.first_name}
last_name: {message.from_user.last_name}
full_name: {message.from_user.full_name}
username: {message.from_user.username}
    ''', reply_markup=start_markup)

async def image_sender(message: types.Message):
    a= randint(1, 2)
    if a == 1:
        await message.answer_photo(open('C:/Users/Sabina/Pictures/о.jpg', 'rb'))
    else:
        await message.answer_photo(open('C:/Users/Sabina/Pictures/р.jpg', 'rb'))

async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'''
/start - запуск
/help - помощь
/myinfo - обо мне
/picture - рандом картина
    ''', reply_markup=start_markup)

def register_handlers_clients(dp: Dispatcher):
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(myinfo, commands="myinfo")
    dp.register_message_handler(image_sender, commands="picture")
    dp.register_message_handler(help, commands="help")
    '''напоминалка'''
    dp.register_message_handler(s_command, Text(startswith="Напомни"))
    '''отправка машин'''
    dp.register_message_handler(show_cars, commands="cars")