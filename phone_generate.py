import random

from file_funcions import listfilewriter


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


phone_list = []
counter = 0

while len(phone_list) < 100000:
    counter += 1
    if counter % 1000 == 0:
        print(counter)
    random_phone = random_phone_num(phone_prefix="+7928")
    random_phone = random_phone + "\n"
    if random_phone in phone_list:
        continue
    phone_list.append(random_phone)


print(counter)

listfilewriter(file_name='megaphone.txt', input_list=phone_list)








