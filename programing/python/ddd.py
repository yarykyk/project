from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import randint
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio
import requests
#import base_poj as dat


token = '5829637736:AAHVOZyuQvKNNy34ApJdblwUYYat8XVhz28'

bot = Bot(token)
dp = Dispatcher()
#
# @dp.message(Command('start'))
# async def start(message:Message):
#     id = message.from_user.id
#     print(id)
#     dat.conect(id=id)
#     if dat.conect(id):
#         await message.showerror('Error', 'ID already exists')
#     else:
#         dat.balance(id)
#         await message.showinfo('Баланс оновлено')
#
# @dp.message()
# async def money(message:Message):
#     await message.answer('Ваш баланс тепер: ')

balance = 0

@dp.message(Command('balance'))
async def start(message:Message):
    await message.answer('Ваш баланс: 0 \n Введіть зміни вашого бюджету: ')


@dp.message()
async def wallet(message:Message):
    global balance
    try:
        change = int(message.text)
        balance += change
        await message.answer(f"Ваш баланс: {balance}грн")
    except ValueError:
        await message.answer("Вводьте лише числа")

@dp.message(Command('exchange'))
async def ask(message:Message):
    kb = [
        [KeyboardButton(text='Австралійський долар')],
        [KeyboardButton(text='Канадський долар')],
        [KeyboardButton(text='Юань Женьміньбі')],
        [KeyboardButton(text='Чеська крона')],
        [KeyboardButton(text='Форинт')],
        [KeyboardButton(text='Теньге')],
        [KeyboardButton(text='Вона')],
        [KeyboardButton(text='Новозеландський долар')],
        [KeyboardButton(text='"Російський рубль')],
        [KeyboardButton(text='Сінгапурський долар')],
        [KeyboardButton(text='Єгипетський фунт')],
        [KeyboardButton(text='Фунт стерлінгів')],
        [KeyboardButton(text='Долар США')],
        [KeyboardButton(text='Турецька ліра')],
        [KeyboardButton(text='Євро')],
        [KeyboardButton(text='Злотий')]

        ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='У яку валюту ви хочете конвертувати ваші гроші?')
    await message.answer("У яку валюту ви хочете конвертувати ваші гроші?", reply_markup=keyboard)


@dp.message(F.text.lower() == 'Австралійський долар')
async def help(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[0]['rate']
    await message.answer(f'{balance}UAH = {exchgeange_rate}AUD', reply_markup=ReplyKeyboardRemove())


# @dp.message(F.text.lower() == 'так')
# async def help(message:Message):
#     url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json'
#     response = requests.get(url)
#     data = response.json()
#     exchange_rate = data[0]['rate']
#     await message.answer(f'Ваш баланс {balance*exchange_rate}', reply_markup=ReplyKeyboardRemove())
#

async def main():
    print('bot is active')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())