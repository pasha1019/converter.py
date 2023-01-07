import requests
import date_curs
import markups as mks
import logging


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
@dp.message_handler(lambda message: message.text == "Курс валют на сегодня")
async def bot_messages(msg: types.Message):
    # Курс на сегодня
    await bot.send_message(msg.from_user.id, f'{date_curs.answer}\nЕвро ={str(eur_curs)}\nДоллар = {str(usd_curs)}')


@dp.message_handler(lambda message: message.text == "Конвертер валют")
async def bot_messages(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Выберите валюту для конвертации\n', reply_markup=mks.convert_menu)


@dp.message_handler(lambda message: message.text == "Информация")
async def bot_messages(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Курс валют предоставлен Центробанком РФ\n', reply_markup=mks.main_menu)


@dp.message_handler(lambda message: message.text == "Конвертировать рубли в доллары")
async def convert_usd(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Введите сумму')

    @dp.message_handler()
    async def convert(msg: types.Message):
        convert_valute = int(msg.text) / usd_curs
        await bot.send_message(msg.from_user.id, f'Получилось {float("{0:.1f}".format(convert_valute))} USD')


@dp.message_handler(lambda message: message.text == "Конвертировать рубли в евро")
async def convert_usd(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Введите сумму')

    @dp.message_handler()
    async def convert(msg: types.Message):
        convert_valute = int(msg.text) / eur_curs
        await bot.send_message(msg.from_user.id, f'Получилось {float("{0:.1f}".format(convert_valute))}EUR')


# Обработка команды help
@dp.message_handler(commands=['help'])
async def help_handler(msg: types.Message):
    await bot.send_message(msg.from_user.id, '''
    /start - выводит главное меню
    /help - выводит справку
    'Курс валют на сегодня' - информирует о курсе доллара и евро на сегодняшнюю дату
    'Конвертер валют' - выводит меню возможных расчетов
    'Конвертировать рубли в' - выберите тип конвертации и введите значение в рублях для конвертации
    'Информация' - общие сведения
    ''')


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")


# Накопление сообщений
if __name__ == '__main__':
    executor.start_polling(dp)
