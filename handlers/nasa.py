from aiogram import Router, types
from aiogram.filters import Command
from utils.nasa_api import get_random_apod

router = Router()
"""
Роутер nasa: команда /space — случайное космическое фото дня (APOD).
"""


@router.message(Command("space"))
async def random_apod(message: types.Message) -> None:
    """
    Обработка команды /space. Показывает случайное фото дня от NASA (APOD).
    Если сегодня видео — сообщает об этом.
    """
    apod = await get_random_apod()

    # Если у APOD бывает видео (media_type == "video"), игнорируем его – только фото
    if apod.get("media_type") != "image":
        await message.answer("🙈 Сегодня у NASA видео, попробуйте ещё раз!")
        return

    await message.answer_photo(photo=apod["url"], caption=apod["title"])
