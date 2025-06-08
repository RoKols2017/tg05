# config.py
"""
Модуль конфигурации: загрузка переменных окружения и настройка параметров через pydantic.
"""
from pathlib import Path
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(Path(__file__).with_name(".env"))

class Settings(BaseSettings):
    """
    Класс настроек приложения. Загружает токены и ключи API из .env.
    """
    bot_token: str
    the_cat_api_key: str
    nasa_api_key: str

    # pydantic-v2: конфигурация через model_config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

config = Settings()  # Глобальный объект конфигурации
