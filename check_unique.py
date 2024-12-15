from file_funcions import filereader


x = filereader(file_name='megaphone.txt')

y = x.split('\n')
z = set(y)
l = len(y) - len(z)
print(l)

