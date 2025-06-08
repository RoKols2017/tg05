import random
from datetime import datetime, timedelta

import aiohttp
from config import config

APOD_URL = "https://api.nasa.gov/planetary/apod"

"""
Модуль для работы с NASA APOD API: получение случайного фото дня.
"""

async def get_random_apod() -> dict:
    """
    Получает случайное фото дня (APOD) за последний год.
    :return: словарь с данными APOD
    """
    end = datetime.utcnow()
    start = end - timedelta(days=365)
    random_date = start + (end - start) * random.random()
    date_str = random_date.strftime("%Y-%m-%d")

    params = {"api_key": config.nasa_api_key, "date": date_str}

    async with aiohttp.ClientSession() as session:
        async with session.get(APOD_URL, params=params, timeout=15) as resp:
            resp.raise_for_status()
            return await resp.json()
