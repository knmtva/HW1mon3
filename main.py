from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging
from random import randint

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'Привет, {message.from_user.first_name}, я буду вашим собеседником')
    await message.delete()

@dp.message_handler(commands=['myinfo'])
async def myinfo(message: types.Message):
    await bot.send_message(message.from_user.id, f'''
id: {message.from_user.id}
first_name: {message.from_user.first_name}
last_name: {message.from_user.last_name}
full_name: {message.from_user.full_name}
username: {message.from_user.username}
    ''')


@dp.message_handler(commands=['picture'])
async def image_sender(message: types.Message):
    a=randint(1, 2)
    if a == 1:
        await message.answer_photo(open('C:/Users/Sabina/Pictures/о.jpg', 'rb'))
    else:
        await message.answer_photo(open('C:/Users/Sabina/Pictures/р.jpg', 'rb'))

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'''
/start - запуск
/help - помощь
/myinfo - обо мне
/picture - рандом картина
    ''')

@dp.message_handler()
async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)


if __name__== '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)