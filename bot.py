import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Tokenni Hugging Face Secrets'dan o'qiymiz
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! Hugging Face Secrets ga BOT_TOKEN ni qo'shganingizga amin bo'ling.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Salom! Men tayyorman. Menga xabar yozishing mumkin!")

@dp.message()
async def echo_message(message: types.Message):
    # Bu yerga o'zingning xohlagan javob logikangni yoki API ulanishlaringni qo'shishing mumkin
    user_text = message.text
    await message.answer(f"Siz yozdingiz: {user_text}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
