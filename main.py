import logging
from config import dp
from aiogram.utils import executor
from handlers import client, extra, callback

client.register_handlers_clients(dp)
callback.register_handlers_callback(dp)
extra.register_extra_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)