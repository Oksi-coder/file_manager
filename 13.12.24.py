'''
Используя список телефонов, создать два новых списка с теми же номерами телефонов, но
сменить оператора. Певый список МТС 918 и назвать файл МТС numbers.txt
Второй Tele-2 908 и назвать файл аналогично.

'''


from check_unique import filereader

phone_number_list = filereader()
phone_number_list = phone_number_list.split('\n')

mts_list =[]
tele2_list = []

for i in phone_number_list:
    new_num1 = i.replace("+7928", "+7918")
    mts_list.append(new_num1 + "\n")

with open("mts.numbers.txt", "w") as _file:
    _file.writelines(mts_list)

for i in phone_number_list:
    new_num = i.replace("+7928", "+7908")
    tele2_list.append(new_num + "\n")

with open("tele2.numbers.txt", "w") as _file:
    _file.writelines(tele2_list)




# def summ2_nums(x: int, y: int) -> int:
#     summ = x + y
#     return summ
#
#
# print(summ2_nums(4,9))


from check_unique import filereader

sp = filereader()
sp = sp.split("\n")

sp2 = []
for i in sp:
    if i.endswith("7777"):
        sp2.append(i)
print(sp2)
print(len(sp2))

