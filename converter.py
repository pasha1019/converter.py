import requests
import date_curs
import markups as mks


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Работа с токеном бота
TOKEN = "*"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Парсинг и присвоение данных курсов валют
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
usd_curs = data['Valute']['USD']['Value']
eur_curs = data['Valute']['EUR']['Value']


# Обработка команды start
@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Привет!\n', reply_markup=mks.main_menu)



# Обработка команд входящих сообщений
@dp.message_handler()
async def bot_messages(msg: types.Message):
    # Проверка команд главного меню
    if msg.text == 'Курс валют на сегодня':
        await bot.send_message(msg.from_user.id, f'{date_curs.answer}\nЕвро = {str(eur_curs)}\nДоллар = {str(usd_curs)}')
    elif msg.text == 'Конвертер валют':
        await bot.send_message(msg.from_user.id, 'Выберите валюту для конвертации.\n', reply_markup=mks.convert_menu)
    elif msg.text == 'Информация':
        pass
    else:
        await bot.send_message(msg.from_user.id, 'Я Вас не понимаю!')


# Обработка команды help
@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    pass


# Накопление сообщений
if __name__ == '__main__':
    executor.start_polling(dp)
