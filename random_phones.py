"""
1. Прочитать три файла.
2. Записать данные из этих файлов в три списка.
3. Из каждого списка выбрать по 3333 случайных номера.
4. Смешать полученные номера хаотично в одном списке.
5. Записать полученный список в новый файл random.txt
"""

import random

from file_funcions import filereader, listfilewriter


st_megafone = filereader('megafone.txt')
sp_megafone = st_megafone.split('\n')

sp_1 = []
for phones in range(3333):
    megafone = random.choice(sp_megafone)
    sp_1.append(megafone + '\n')


st_mts = filereader('mts.txt')
sp_mts = st_mts.split('\n')

sp_2 = []
for phones in range(3333):
    mts = random.choice(sp_mts)
    sp_2.append(mts + '\n')


st_t2 = filereader('t2.txt')
sp_t2 = st_t2.split('\n')

sp_3 = []
for phones in range(3333):
    t2 = random.choice(sp_t2)
    sp_3.append(t2 + '\n')

random_list = sp_1 + sp_2 + sp_3
random.shuffle(random_list)

print(len(random_list))

listfilewriter('random.txt', random_list)
