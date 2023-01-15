from config import bot
from aiogram import Dispatcher, types

async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)

def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
