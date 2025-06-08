# utils/cat_api.py
"""
Модуль для работы с TheCatAPI: получение пород, поиск, получение фото по породе.
"""
import aiohttp
from config import config

BASE = "https://api.thecatapi.com/v1"
HEADERS = {"x-api-key": config.the_cat_api_key}


async def _fetch_json(url: str) -> dict | list:
    """
    Вспомогательная функция: выполняет GET-запрос и возвращает JSON.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, timeout=15) as resp:
            resp.raise_for_status()
            return await resp.json()


# ---------- ПОЛНЫЙ СПИСОК ПОРОД ----------
async def get_breeds() -> list[dict]:
    """
    Возвращает список всех пород кошек с TheCatAPI.
    """
    return await _fetch_json(f"{BASE}/breeds")


# ---------- ПОИСК ПОРОДЫ -----------------
async def find_breed(en_query: str) -> dict | None:
    """
    Ищет породу, пытаясь сопоставить `en_query` сначала точным, затем частичным совпадением.
    :param en_query: название породы на английском
    :return: словарь с данными породы или None
    """
    q = en_query.lower()
    for breed in await get_breeds():
        if breed["name"].lower() == q:          # точное
            return breed
    for breed in await get_breeds():
        if q in breed["name"].lower():          # частичное
            return breed
    return None


# ---------- КАРТИНКА ПО ID ---------------
async def get_cat_image_by_breed(breed_id: str) -> str:
    """
    Возвращает URL картинки кошки по ID породы.
    :param breed_id: идентификатор породы
    :return: URL изображения
    """
    data = await _fetch_json(f"{BASE}/images/search?breed_ids={breed_id}")
    return data[0]["url"] if data else ""



async def get_breed_by_id(breed_id: str) -> dict | None:
    """
    Возвращает словарь с данными породы по её ID.
    :param breed_id: идентификатор породы
    :return: словарь с данными породы или None
    """
    for breed in await get_breeds():
        if breed["id"] == breed_id:
            return breed
    return None