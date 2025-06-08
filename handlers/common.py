from aiogram import Router, types
from aiogram.filters import CommandStart, Command

router = Router()
"""
Роутер common: стартовые и справочные команды.
"""


@router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    """
    Обработка команды /start. Приветствие и краткая справка.
    """
    await message.answer(
        "🐾 <b>Привет!</b>\n"
        "Я помогу узнать всё о породах кошек и покажу красоту космоса.\n\n"
        "📋 <b>Команды:</b>\n"
        "• <b>/cats</b> — пришлю 10 случайных пород (кнопки, можно нажимать)\n"
        "• <b>/space</b> — случайное космическое фото дня 🚀\n"
        "• <b>/help</b> — краткая справка\n\n"
        "💬 Просто отправь название породы на русском или английском, "
        "и я пришлю фото и описание."
    )


@router.message(Command("help"))
async def cmd_help(message: types.Message) -> None:
    """
    Обработка команды /help. Краткая справка по возможностям бота.
    """
    await message.answer(
        "/start – приветствие\n"
        "/help  – эта справка\n"
        "/cats  – 10 случайных пород кошек\n"
        "/space – случайный APOD (NASA)\n\n"
        "Или просто отправьте название породы кошки."
    )
