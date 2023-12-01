import asyncio
import logging
import os
import sys

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from handlers import (get_to_menu_and_get_report,
                      commands,
                      direction,
                      my_profile,
                      manage_users)

load_dotenv()
telegram_id = None


async def main() -> None:
    dp = Dispatcher()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.warning(f"Bot start")

    dp.include_routers(
        commands.router,
        get_to_menu_and_get_report.router,
        my_profile.router,
        manage_users.router,
        direction.router
    )

    bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())