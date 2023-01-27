from config import bot, Dispatcher
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.base import get_products

kb_menu = InlineKeyboardMarkup()
kb_menu.add(
    InlineKeyboardButton("salaty", callback_data="salate_sender"),
    InlineKeyboardButton("drinks", callback_data="drink_sender")
)

def buy_kb(product_id):
    buy = InlineKeyboardMarkup()
    buy.add(InlineKeyboardButton('Купить', callback_data=f'fsm_start {product_id}'))
    return buy

tovar1 = get_products()[0]
tovar2 = get_products()[1]
tovar3 = get_products()[2]
tovar4 = get_products()[3]

async def menu_sender(call: types.CallbackQuery):
    photo = open("media/photo.png", "rb")
    await call.bot.send_photo(call.from_user.id, photo, reply_markup=kb_menu)
    photo.close()



async def salate_sender(call: types.CallbackQuery):
    photo = open(f'{tovar1[4]}', 'rb')
    await call.bot.send_photo(chat_id=call.from_user.id, caption=f'{tovar1[1]}\n'
                                                                 f'{tovar1[2]}\n'
                                                                 f'Цена: {tovar1[3]}', photo=photo,
                              reply_markup=buy_kb(tovar1[0]))

    photo1 = open(f'{tovar2[4]}', 'rb')
    await call.bot.send_photo(chat_id=call.from_user.id, caption=f'{tovar2[1]}\n'
                                                                 f'{tovar2[2]}\n'
                                                                 f'Цена: {tovar2[3]}', photo=photo1,
                              reply_markup=buy_kb(tovar2[0]))
async def drink_sender(call: types.CallbackQuery):
    photo2 = open("media/mimoza.jpg", "rb")
    photo3 = open("media/blue.jpg", "rb")
    await call.bot.send_photo(chat_id=call.from_user.id, caption=f'{tovar3[1]}\n'
                                                                 f'{tovar3[2]}\n'
                                                                 f'Цена: {tovar3[3]}', photo=photo2,
                              reply_markup=buy_kb(tovar4[0]))

    await call.bot.send_photo(chat_id=call.from_user.id, caption=f'{tovar4[1]}\n'
                                                                 f'{tovar4[2]}\n'
                                                                 f'Цена: {tovar4[3]}', photo=photo3,
                              reply_markup=buy_kb(tovar4[0]))


async def address_sender(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Мы находимся по адресу Фучика, 34")

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(menu_sender, text="button_call_1")
    dp.register_callback_query_handler(address_sender, text="button_call_2")
    dp.register_callback_query_handler(salate_sender, text="salate_sender")
    dp.register_callback_query_handler(drink_sender, text="drink_sender")


