from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import base_poj as dat



token = '5829637736:AAHVOZyuQvKNNy34ApJdblwUYYat8XVhz28'

bot = Bot(token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(f"Привіт, зараз твій баланс: {}")

async def main():
    print('bot is active')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())