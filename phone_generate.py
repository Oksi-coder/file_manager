import random

from json_functions import write_json


def random_phone_num(phone_prefix: str) -> str:
    """
    Функция генерирует случайный номер телефона на основе полученного префикса.

    :param phone_prefix: Первые 4 цифры номера, начиная "+". Пример: "+7928".
    :return: Случайный номер телефона. Пример: "+79285674839".
    """
    for _ in range(7):
        num = random.randint(0, 9)
        phone_prefix += str(num)
    return phone_prefix


def phone_list_generator(phone_count: int, phone_prefix: str) -> list[str]:
    phone_list = []
    counter = 0

    while len(phone_list) < phone_count:
        counter += 1
        if counter % 1000 == 0:
            print(counter)
        random_phone = random_phone_num(phone_prefix)
        if random_phone in phone_list:
            continue
        phone_list.append(random_phone)

    print(counter)

    return phone_list


main_data = {
    'megaphone.json': '+7928',
    'mts.json': '+7918',
    't2.json': '+7908',
}

for file_name, prefix in main_data.items():
    x = phone_list_generator(10000, prefix)
    write_json(x, file_name)
