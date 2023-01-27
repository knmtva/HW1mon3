from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buy_item_kb = InlineKeyboardMarkup()
buy_item_kb.add(
    InlineKeyboardButton('Купить', callback_data='buy_item')
)

async def show_books(message: types.Message):
    await message.answer(text="Вот наше меню:")
    await message.answer(text="Цезарь", reply_markup=buy_item_kb)
    await message.answer(text="Оливье", reply_markup=buy_item_kb)
    await message.answer(text="Мимоза", reply_markup=buy_item_kb)
    await message.answer(text="Голубая лагуна", reply_markup=buy_item_kb)