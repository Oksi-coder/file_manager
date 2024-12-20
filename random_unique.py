import random

from phone_generate import phone_list_generator

from file_funcions import listfilewriter


mts_sp = phone_list_generator(3333, '+7928')
t2_sp = phone_list_generator(3333, '+7908')
megafone_sp = phone_list_generator(3333, '+7918')

random_unique_sp = mts_sp + t2_sp + megafone_sp
random.shuffle(random_unique_sp)

listfilewriter('random_unique.txt', random_unique_sp)




