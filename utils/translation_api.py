# utils/translation_api.py
"""
Модуль для перевода текста через MyMemory API.
"""
import aiohttp
from typing import Final

MEMORY_URL: Final = "https://api.mymemory.translated.net/get"


async def translate(text: str, src: str = "en", dest: str = "ru") -> str:
    """
    Переводит `text` с помощью MyMemory.
    :param text: исходный текст
    :param src: язык-источник (по умолчанию 'en')
    :param dest: язык-приёмник (по умолчанию 'ru')
    :return: переведённая строка или исходный текст при ошибке
    """
    params = {"q": text, "langpair": f"{src}|{dest}"}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(MEMORY_URL, params=params, timeout=15) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data["responseData"]["translatedText"]
    except Exception:
        # fallback: отдаём оригинальный английский
        return text
