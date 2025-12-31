from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import *

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(
        "👋 Witaj!\n\n"
        "🎧 Dostęp Spotify Family\n"
        f"💰 Cena: {PRICE}\n\n"
        "Napisz: kup"
    )

@dp.message_handler(lambda m: m.text.lower() == "kup")
async def buy(msg: types.Message):
    await msg.answer(
        f"💳 Płatność:\n"
        f"BLIK: {BLIK_NUMBER}\n"
        f"Konto: {BANK_ACCOUNT}\n\n"
        f"Po płatności napisz: opłacone"
    )

@dp.message_handler(lambda m: m.text.lower() == "opłacone")
async def paid(msg: types.Message):
    await bot.send_message(
        ADMIN_ID,
        f"💰 Nowa płatność od @{msg.from_user.username}"
    )
    await msg.answer("✅ Dzięki! Sprawdzę płatność.")

executor.start_polling(dp)
