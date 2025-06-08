# handlers/cats.py
"""
Роутер cats: обработка поиска и вывода информации о породах кошек.
"""
from aiogram import Router, types, F
from utils.cat_api import (
    find_breed, get_breed_by_id,
    get_cat_image_by_breed
)
from utils.translation_api import translate

router = Router()

# ---------- 1. callback_query от кнопок /cats ----------
@router.callback_query(F.data.startswith("breed:"))
async def callback_breed(query: types.CallbackQuery) -> None:
    """
    Обработка callback-запроса по породе кошки (кнопка из /cats).
    Показывает фото и описание выбранной породы.
    """
    breed_id = query.data.split(":", 1)[1]
    breed = await get_breed_by_id(breed_id)

    if not breed:
        await query.answer("Не удалось найти породу.", show_alert=True)
        return

    desc_ru = await translate(breed["description"], src="en", dest="ru")
    photo_url = await get_cat_image_by_breed(breed_id)

    caption = (
        f"<b>Порода:</b> {breed['name']}\n"
        f"<b>Описание:</b> {desc_ru}\n"
        f"<b>Продолжительность жизни:</b> {breed['life_span']} лет"
    )

    await query.message.answer_photo(photo=photo_url, caption=caption)
    await query.answer()  # закрываем «часики» Telegram

# ---------- 2. текстовый ввод (осталось как было) -------
@router.message(F.text & ~F.text.startswith("/"))
async def breed_info(message: types.Message) -> None:
    """
    Обработка текстового сообщения: поиск породы по названию (рус/англ).
    """
    user_text = message.text.strip()
    en_query = await translate(user_text, src="ru", dest="en")

    breed = await find_breed(en_query)
    if not breed:
        await message.answer("❌ Порода не найдена. Попробуйте ещё раз.")
        return

    desc_ru = await translate(breed["description"], src="en", dest="ru")
    photo_url = await get_cat_image_by_breed(breed["id"])

    caption = (
        f"<b>Порода:</b> {breed['name']}\n"
        f"<b>Описание:</b> {desc_ru}\n"
        f"<b>Продолжительность жизни:</b> {breed['life_span']} лет"
    )
    await message.answer_photo(photo=photo_url, caption=caption)
