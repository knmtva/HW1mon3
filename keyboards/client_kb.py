from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/myinfo")
help_button = KeyboardButton("/help")

start_markup.add(start_button, info_button, help_button)