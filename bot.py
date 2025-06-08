"""
Основной модуль запуска Telegram-бота на aiogram.
Регистрирует роутеры и запускает polling.
"""
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import config
from handlers import common, cats, nasa, cats_list


def register_routers(dp: Dispatcher) -> None:
    """
    Регистрирует все роутеры (обработчики команд и событий) в диспетчере.
    :param dp: Dispatcher — диспетчер aiogram
    """
    dp.include_router(common.router)
    dp.include_router(nasa.router)
    dp.include_router(cats_list.router)  # /cats
    dp.include_router(cats.router)



async def main() -> None:
    """
    Точка входа: инициализация бота и запуск polling.
    """
    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
