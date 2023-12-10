
from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phones.csv'

## ЗАДАНИЕ НЕ ДОДЕЛАНО!

def get_info():
    first_name = 'Иван'
    last_name = 'Иванов'
    phone_number = None

    is_valid = False

    while not is_valid:
        try: 
            phone_number = 99999999999
            if len(str(phone_number)) != 11:
                print('Не верная длина номера')
            else: 
                is_valid = True
        except ValueError:
            print('Не валидный номер')

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def write_file(lst):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)

    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        res.append(obj)
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def main():
    while True:
        command = input('Введите команду:')

        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует')
                continue
            print(*read_file(file_name))

main()