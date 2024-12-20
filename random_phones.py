"""
1. Прочитать три файла.
2. Записать данные из этих файлов в три списка.
3. Из каждого списка выбрать по 3333 случайных номера.
4. Смешать полученные номера хаотично в одном списке.
5. Записать полученный список в новый файл random.txt



1. Проверить на уникальность новый файл.
2. Сделать, чтобы телефоны были уникальными.
"""

import random

from json_functions import read_json, write_json


def numbers_3333(operator: str):
    list_telephones = read_json(operator)

    new_list = []
    while len(new_list) < 3333:
        phone_number = random.choice(list_telephones)
        if phone_number in new_list:
            continue
        new_list.append(phone_number)

    return new_list


list_1 = numbers_3333('megaphone.json')
list_2 = numbers_3333('mts.json')
list_3 = numbers_3333('t2.json')

random_list = list_1 + list_2 + list_3
random.shuffle(random_list)

write_json(random_list, 'random.json')
