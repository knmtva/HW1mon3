import logging
import asyncio
from config import dp
from handlers.zinzin import binbon
from aiogram.utils import executor
from handlers import client, extra, callback,admin, fsm_anketa
from cars.pars import par_car
from db.base import (
init,
create_tables
)

from cars.db_cars import (
init1,
create_tables1
)



fsm_anketa.register_handlers_anketa(dp)
client.register_handlers_clients(dp)
callback.register_handlers_callback(dp)
admin.register_admin_handlers(dp)
extra.register_extra_handlers(dp)

async def startup(_):
    init()
    create_tables()
    asyncio.create_task(binbon())
    init1()
    create_tables1()
    par_car()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=startup)