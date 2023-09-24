import asyncio
from aiogram import Bot, Dispatcher
from app import models as db
from app.handlers import router


async def main():
    TOKEN = "5751662917:AAGaVh6m6BWrWViGo1vhp0OP9BCGxtdcXXo"

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await db.db_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("Конец работы программы")
