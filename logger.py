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
    search = input('Поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf_8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            new_item = item.replace('Город:', ' ').split()
            if search in new_item[index]:
                print(item, end='\n\n')

def print_data():
    with open('book.txt', 'r', encoding='utf_8') as file:
        print(file.read())

def change_data():
    print('Выберите вариант поиска контакта, чью информацию вы хотите изменить:\n'
          '1 - Фамилия\n'
          '2 - Имя\n'
          '3 - Отчество\n'
          '4 - Номер телефона\n'
          '5 - Адрес\n')
    index = int(input('Выберите действие: ')) - 1
    search = input('Введите данные поиска: ').title()
    replacement = input('Введите данные для замены: ').title()
    with open('book.txt', 'r', encoding='utf_8') as file:
        data = file.read().strip().split('\n\n')
    
    new_data = []
    my_check = False

    for item in data:
        contact_info = item.replace('\n', ' ').split()
        if len(contact_info) >= index + 1:
            if contact_info[index] == search:
                my_check = True
                contact_info[index] = replacement
                new_data.append(
                    f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n+7{contact_info[3]}\nГород: {contact_info[4]}\n\n')
            else:
                new_data.append(item)
        else:
            new_data.append(item)
    
    if not my_check:
        print('Совпадений не найдено. Введите корректные данные')

    with open('book.txt', 'w', encoding='utf_8') as file:
        file.write('\n'.join(new_data))

def delete_data():
    print('Выберите вариант поиска контакта, которого хотите удалить:\n'
          '1 - Фамилия\n'
          '2 - Имя\n'
          '3 - Отчество\n'
          '4 - Номер телефона\n'
          '5 - Адрес\n'
          '6 - Удалить контакт целиком\n')
    index = int(input('Выберите действие: ')) - 1
    search_to_delete = input('Введите данные удаления: ').title()
    with open('book.txt', 'r', encoding='utf_8') as file:
        data = file.read().strip().split('\n\n')
    
    new_data = []

    for item in data:
        if search_to_delete in item:

            if index < 5:
                contact_info = item.replace('\n', ' ').split()
                if len(contact_info) >= index + 1 and search_to_delete == contact_info[index]:
                    contact_info[index] = 'deleted'
                    # new_data.append(' '.join(contact_info[:3]) + '\n'.join(contact_info[3:]))
                    new_data.append(f'{contact_info[0]} {contact_info[1]} {contact_info[2]}\n+7{contact_info[3]}\nГород: {contact_info[4]}\n\n')
                else:
                    new_data.append(item)
        else:
            new_data.append(item) 
        
    with open('book.txt', 'w', encoding='utf_8') as file:
        file.write('\n'.join(new_data))