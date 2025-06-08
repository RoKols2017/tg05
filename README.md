# 🐾 My Cat Space Bot

Telegram‑бот, который совмещает **милых котиков** и **красоту космоса**.  
Построен на [`aiogram` 3.20.0post0](https://docs.aiogram.dev/en/latest/).

| Команда / действие | Что делает |
|--------------------|-----------|
| `/start`, `/help`  | Приветствие и справка |
| `/cats`            | Выводит 10 случайных пород с кнопками |
| Нажатие на кнопку  | Присылает фото и описание породы на русском |
| `<текст>`          | Поиск породы (можно писать по‑русски) |
| `/space`           | Случайное «Astronomy Picture of the Day» (NASA) |

---

## ✨ Ключевые особенности

* **Интерактивный список пород** — `/cats` формирует клавиатуру из 10 случайных пород.  
* **Двусторонний перевод**  
  * Ввод `ru → en` для поиска в TheCatAPI  
  * Описание `en → ru` перед отправкой пользователю  
  * Бесплатный сервис MyMemory, без API‑ключа  
* Асинхронный, типизированный код, разделённый на `handlers/` и `utils/`.  
* Настройки и ключи храните в `.env`, не публикуйте в GitHub.

---

## 🗂 Структура проекта

```text
my_cat_space_bot/
├── bot.py                 # точка входа
├── config.py              # pydantic + dotenv
├── .env.example           # шаблон переменных окружения
├── requirements.txt
├── handlers/
│   ├── __init__.py
│   ├── common.py          # /start, /help
│   ├── cats_list.py       # /cats – клавиатура
│   ├── cats.py            # поиск + callback
│   └── nasa.py            # /space
└── utils/
    ├── __init__.py
    ├── cat_api.py         # TheCatAPI
    ├── nasa_api.py        # NASA APOD
    └── translation_api.py # MyMemory
```

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/your-name/my_cat_space_bot.git
cd my_cat_space_bot

python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env            # заполните токены и ключи
python bot.py
```

### Пример `.env`

```dotenv
BOT_TOKEN=123456:ABCDEF...
THE_CAT_API_KEY=cat_xxxxxxxxxxxxxxxxx
NASA_API_KEY=DEMO_KEY
```

---

## ☁️ Запуск в Docker

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

```bash
docker build -t cat-space-bot .
docker run -d --env-file .env cat-space-bot
```

---

## 🤝 Вклад

PR‑ы приветствуются: новые команды, тесты, поддержка других API!

---

## ⚖️ Лицензия

MIT

---

## 🙏 Благодарности

* **TheCatAPI** — котики.  
* **NASA APOD** — космос.  
* **MyMemory** — бесплатный перевод.  
* **aiogram** — любимый фреймворк.
