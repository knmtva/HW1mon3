from config import bot
from aiogram import Dispatcher, types

async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

def register_extra_handlers(dp: Dispatcher):
    dp.register_message_handler(echo)
