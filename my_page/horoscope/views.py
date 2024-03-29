from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries':
        {'description': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
         'types': 'fire',
         'day_start': 21,
         'month_start': 3,
         'day_finish': 20,
         'month_finish': 4
         },
    'taurus':
        {'description': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
         'types': 'earth',
         'day_start': 21,
         'month_start': 4,
         'day_finish': 21,
         'month_finish': 5
         },
    'gemini':
        {'description': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
         'types': 'air',
         'day_start': 22,
         'month_start': 5,
         'day_finish': 21,
         'month_finish': 6
         },
    'cancer':
        {'description': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
         'types': 'water',
         'day_start': 22,
         'month_start': 6,
         'day_finish': 22,
         'month_finish': 7
         },
    'leo':
        {'description': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 7,
         'day_finish': 21,
         'month_finish': 8
         },
    'virgo':
        {'description': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
         'types': 'earth',
         'day_start': 22,
         'month_start': 8,
         'day_finish': 23,
         'month_finish': 9
         },
    'libra':
        {'description': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
         'types': 'air',
         'day_start': 24,
         'month_start': 9,
         'day_finish': 23,
         'month_finish': 10
         },
    'scorpio':
        {'description': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
         'types': 'water',
         'day_start': 24,
         'month_start': 10,
         'day_finish': 22,
         'month_finish': 11
         },
    'sagittarius':
        {'description': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
         'types': 'fire',
         'day_start': 23,
         'month_start': 11,
         'day_finish': 22,
         'month_finish': 12
         },
    'capricorn':
        {'description': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
         'types': 'earth',
         'day_start': 23,
         'month_start': 12,
         'day_finish': 20,
         'month_finish': 1
         },
    'aquarius':
        {'description': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
         'types': 'air',
         'day_start': 21,
         'month_start': 1,
         'day_finish': 19,
         'month_finish': 2
         },
    'pisces':
        {'description': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
         'types': 'water',
         'day_start': 20,
         'month_start': 2,
         'day_finish': 20,
         'month_finish': 3
         }
}

zodiac_types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

number_of_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

for_navbar = dict()
for key, val in zodiac_dict.items():
    for_navbar[key] = val['description']


def get_zodiac_info(request, zodiac_value):
    description = zodiac_dict.get(zodiac_value)
    # Присвоим переменной значение по названию знака зодиака
    if description:
        description_value = description['description']
    else:
        description_value = None
    # Так как здесь словарь со вложенными словарями, то в случае успешнога поиска значения по ключу,
    # присвоим его переменной description_value. Но если поиск безуспешен, присвоим этой же переменной значение None,
    # иначе будет ошибка TypeError, так как объект None не является словарем.
    # Именно переменную description_value помещаем в словарь, чтобы использовать в дальнейшем.
    data = {
        'description_zodiac': description_value,
        'name': zodiac_value,
        'zodiacs': for_navbar
    }
    # Переменной data присвоим словарь, который мы будем использовать при обращении к его значениям из HTML-файла.
    return render(request, 'horoscope/info_zodiac.html', context=data)
    # С помощью данной функции из модуля django.shortcuts можно объединить процесс трансформации файла в строку и
    # HTTP-ответа. Наряду с роутом эта функция обязательно должна принимать request.
    # Именнованному аргументу context присвоим значение нашего словаря data, с которым мы и будем работать
    # при обращении из HTML-файла.


def get_zodiac_info_by_number(request, zodiac_value: int):
    zodiacs = list(zodiac_dict)
    if zodiac_value > len(zodiacs):
        return HttpResponseNotFound(f'There is no a zodiac sign with number {zodiac_value}!')
    name_zodiac = zodiacs[zodiac_value - 1]
    redirect_url = reverse('horoscope_value', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def index(request):
    types = list(zodiac_types)
    zodiacs = zodiac_dict
    context = {
        'types': types,
        'zodiacs': for_navbar
    }
    return render(request, 'horoscope/index.html', context=context)


def get_zodiac_type_list(request, zodiac_value):
    type_list = zodiac_types.get(zodiac_value)
    zodiacs = zodiac_dict
    if type_list:
        data = {
            'type_list': type_list,
            'zodiacs': for_navbar
        }
        return render(request, 'horoscope/type_list.html', context=data)
    else:
        return get_zodiac_info(request, zodiac_value)


def determine_zodiac_sign(request, month, day):
    if month not in range(1, 13):
        return HttpResponseNotFound('Please, enter valid values!')
    if day not in range(1, number_of_days[month] + 1):
        return HttpResponseNotFound('Please, enter valid values!')
    for sign, info in zodiac_dict.items():
        if month == info['month_start'] and day >= info['day_start'] or \
                month == info['month_finish'] and day <= info['day_finish']:
            return HttpResponse(f'{sign.title()}!')


def determine_zodiac_sign_error(request, month, day):
    return HttpResponseNotFound('Please, enter valid values!')
