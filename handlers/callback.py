from config import bot, Dispatcher
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def menu_sender(call: types.CallbackQuery):

    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("салаты", callback_data="button_call_3")
    button_call_4 = InlineKeyboardButton("напитки", callback_data="button_call_4")
    markup.add(button_call_3, button_call_4)

    photo = open("media/photo.png", "rb")
    await bot.send_photo(call.from_user.id, photo, reply_markup=markup)
    photo.close()

async def salate_sender(call: types.CallbackQuery):
    photo1 = open("media/zez.jpg", "rb")
    photo2 = open("media/olivie.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo1)
    photo1.close()
    await bot.send_message(call.from_user.id, "Цезарь стоит 350 сом")
    await bot.send_photo(call.from_user.id, photo2)
    photo2.close()
    await bot.send_message(call.from_user.id, "Оливье стоит 260 сом")

async def drink_sender(call: types.CallbackQuery):
    photo3 = open("media/mimoza.jpg", "rb")
    photo4 = open("media/blue.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo3)
    photo3.close()
    await bot.send_message(call.from_user.id, "Коктейль Мимоза - 500сом")
    await bot.send_photo(call.from_user.id, photo4)
    photo4.close()
    await bot.send_message(call.from_user.id, "Коктейль Голубая лагуна - 450 сом")

async def address_sender(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Мы находимся по адресу Фучика, 34")

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(menu_sender, text="button_call_1")
    dp.register_callback_query_handler(address_sender, text="button_call_2")
    dp.register_callback_query_handler(salate_sender, text="button_call_3")
    dp.register_callback_query_handler(drink_sender, text="button_call_4")


