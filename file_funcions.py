

def filewritter(file_name: str, input_string: str) -> None:
    file_path = f'data/{file_name}'
    with open(file_path, "a") as _file:
        _file.write(input_string)


def listfilewriter(file_name: str, input_list: list[str]) -> None:
    file_path = f'data/{file_name}'
    with open(file_path, "w") as _file:
        _file.writelines(input_list)


def filereader(file_name: str) -> str:
    file_path = f'data/{file_name}'
    with open(file_path, "r") as _file:
        output_string = _file.read()
    return output_string
