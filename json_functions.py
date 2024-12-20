import json

from file_funcions import filewritter, filereader


def write_json(input_obj: list|dict, file_name: str):
    file_data = json.dumps(input_obj, indent=2)
    filewritter(file_name, file_data)


def read_json(file_name: str):
    file_data = filereader(file_name)
    return json.loads(file_data)
