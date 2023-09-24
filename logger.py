from data_create import *

def enter_data():
    surname = surname_person()
    name = name_person()
    patronymic = patronymic_person()
    num_phone = num_phone_person()
    addres = region_addres_person()
    with open('book.txt', 'a', encoding='utf_8') as file:
        file.write(f'{surname} {name} {patronymic}\n+7{num_phone}\nГород: {addres}\n\n')

def search_data():
    print('Выберите вариант поиска:\n'
          '1 - Фамилия\n'
          '2 - Имя\n'
          '3 - Отчество\n'
          '4 - Номер телефона\n'
          '5 - Адрес\n')
    index = int(input('Выберите вариант: ')) - 1
    search = input('Поисковые данные: ')
    with open('book.txt', 'r', encoding='utf_8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            new_item = item.replace('Город:', ' ').split()
            if search in new_item[index]:
                print(item, end='\n\n')
            else:
                print('Контакт не найден')