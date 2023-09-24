from logger import *

def user_iterface():
    cmd = 0
    while cmd != '6':
        print('Выберите вариант действий:\n'
            '1 - Создать новый контакт\n'
            '2 - Показать все контакты\n'
            '3 - Поиск контакта\n'
            '4 - Изменение данных о контакте\n'
            '5 - Удаление контакта\n'
            '6 - Выход\n')
        cmd = input('Выберите действие: ')
        if cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Неккоректный ввод')
            cmd = input('Выберите действие: ')
        match cmd:
            case '1':
                enter_data()
            # case '2':
            #     print_data()
            case '3':
                search_data()
            # case '4':
            #     change_data()
            # case '5':
            #     delete_data()
            case '6':
                print('Всего доброго!')