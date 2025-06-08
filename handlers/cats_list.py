# handlers/cats_list.py
"""
Роутер cats_list: команда /cats — выводит 10 случайных пород кошек с кнопками.
"""
import random
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils.cat_api import get_breeds

router = Router()


@router.message(Command("cats"))
async def random_cat_breeds(message: types.Message) -> None:
    """
    Обработка команды /cats. Показывает 10 случайных пород кошек с инлайн-кнопками.
    """
    breeds = await get_breeds()
    if not breeds:
        await message.answer("Не удалось получить список пород 😿")
        return

    sample = random.sample(breeds, k=10)

    # --- строим клавиатуру ---
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=b["name"],
                    callback_data=f"breed:{b['id']}"  # передаём ID
                )
            ]
            for b in sample
        ]
    )

    await message.answer(
        "🐱 Выберите породу из списка:",
        reply_markup=kb
    )
