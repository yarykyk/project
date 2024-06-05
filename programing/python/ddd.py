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


@dp.message(F.text.regexp('^\/add .*'))
async def wallet(message: Message):
    global balance
    try:
        a = message.text.split(' ')
        change = int(a[1])
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
        [KeyboardButton(text='Російський рубль')],
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


@dp.message(F.text == 'Австралійський долар')
async def help(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[0]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}AUD', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Канадський долар')
async def help1(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[1]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}CAD', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Юань Женьміньбі')
async def help2(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[2]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}CNY', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Чеська крона')
async def help3(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[3]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}CZK', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Форинт')
async def help4(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[6]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}Ft', reply_markup=ReplyKeyboardRemove())
@dp.message(F.text == 'Теньге')
async def help5(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[11]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}KZT', reply_markup=ReplyKeyboardRemove())
@dp.message(F.text == 'Вона')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[12]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}W', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Новозеландський долар')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[15]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}NZD', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Російський рубль')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[17]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}RUB', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Сінгапурський долар')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[18]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}SGD', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Єгипетський фунт')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[22]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}AUD', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Фунт стерлінгів')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[23]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}EGP', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Долар США')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[24]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}USD', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Турецька ліра')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[28]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}TRY', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Євро')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[31]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}EUR', reply_markup=ReplyKeyboardRemove())

@dp.message(F.text == 'Злотий')
async def help6(message:Message):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    response = requests.get(url)
    data = response.json()
    exchgeange_rate = data[32]['rate']
    await message.answer(f'{balance}UAH = {balance/exchgeange_rate}PLN', reply_markup=ReplyKeyboardRemove())




async def main():
    print('bot is active')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())