from aiogram import types
from config import bot
import asyncio
import aioschedule

async def s_command(message: types.Message):
    global chat_id
    global clock
    clock = message.text[8:]
    chat_id = message.from_user.id
    await message.answer("ok")

async def notice():
    print("yes")
    await bot.send_message(
        chat_id=chat_id,
        text=clock
    )

async def binbon():
    aioschedule.every(5).seconds.do(notice)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)