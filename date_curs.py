import datetime


# Сегодняшнее число
today = datetime.date.today()
dt = datetime.datetime.now()
if dt.weekday() == 0:
    day = 'понедельник'
elif dt.weekday() == 1:
    day = 'вторник'
elif dt.weekday() == 2:
    day = 'среда'
elif dt.weekday() == 3:
    day = 'четверг'
elif dt.weekday() == 4:
    day = 'пятница'
elif dt.weekday() == 5:
    day = 'суббота'
else:
    day = 'воскресенье'


# Получение наименования месяца
if dt.month == 1:
    month_td = 'января'
elif dt.month == 2:
    month_td = 'февраля'
elif dt.month == 3:
    month_td = 'марта'
elif dt.month == 4:
    month_td = 'апреля'
elif dt.month == 5:
    month_td = 'мая'
elif dt.month == 6:
    month_td = 'июня'
elif dt.month == 7:
    month_td = 'июля'
elif dt.month == 8:
    month_td = 'августа'
elif dt.month == 9:
    month_td = 'сентября'
elif dt.month == 10:
    month_td = 'октября'
elif dt.month == 11:
    month_td = 'ноября'
else:
    month_td = 'декабря'


# Формирование приветствия
answer = 'Курсы валют от ЦБ РФ на' + ' ' + str(today.day) + ' ' + month_td + ' ' + '(' + day + ')'
