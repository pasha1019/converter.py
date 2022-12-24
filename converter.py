import requests
import date_curs

# t.me/valute_test_user_bot

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Работа с токеном бота
TOKEN = "5909796694:AAHqK0zVk9-Jl9I_WRuXRNCkejtMTIDukrQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Парсинг и присвоение данных курсов валют
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
usd_curs = data['Valute']['USD']['Value']
eur_curs = data['Valute']['EUR']['Value']


# Обработка команд start
@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer(date_curs.answer + '\n' + 'Евро = ' + str(eur_curs) + '\n' + 'Доллар = ' + str(usd_curs))


# Обработка команд входящих сообщений
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    elif msg.text.lower() == "помоги":
        await msg.answer('Чем помочь?')
    else:
        await msg.answer('Не понимаю, что это значит.')


# Накопление сообщений
if __name__ == '__main__':
    executor.start_polling(dp)
