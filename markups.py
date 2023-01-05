from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_main = KeyboardButton('Главное меню')
# Главное меню
button_1 = KeyboardButton('Курс валют на сегодня')
button_2 = KeyboardButton('Конвертер валют')
button_3 = KeyboardButton('Информация')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1, button_2, button_3)


# Меню конвертации
button_USD = KeyboardButton('Доллар')
button_EUR = KeyboardButton('Евро')
button_RUB = KeyboardButton('Рубль')
convert_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_USD,button_RUB,button_EUR)