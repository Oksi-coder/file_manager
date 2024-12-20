from json_functions import read_json


x = read_json(file_name='random.json')

z = set(x)
print(len(x) - len(z))
