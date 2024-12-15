from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib. fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot,storage = MemoryStorage())

@dp.message_handler(text= "привет")
async def all_message(message):
    await message.answer("Введите команду /start,чтобы начать общение")

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет я бот помогающий твоему здоровью")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)