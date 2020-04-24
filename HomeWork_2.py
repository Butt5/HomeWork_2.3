documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def request_people():
    request = input('Введите номер документа для вывода имени человека, которому он принадлежит: ')
    for request_number in documents:
        if request in request_number.values():
            print(request_number['name'])
            break
    else:
        print('Такого номера не существует')

        # break


# request_people()


def number_shelf():
    doc_number_request = input('Введите номер документа для отображения номера полки, на которой он находится: ')
    for shelf, number in directories.items():
        if doc_number_request in number:
            print(f'Номер полки {shelf}')
            break
    else:
        print('Запрашиваемый документ отсутствует')


def list_documents():
    for format_list in documents:
        print(format_list['type'], '"', format_list['number'], '"', '"', format_list['name'], '"')


# list_documents(format_list)

def add():
    add_type = input('Введите тип документа, например "passport": ')
    add_number = input('Введите номер документа: ')
    add_name = input('Введите фамилию и имя владельца: ')
    add_number_directories = input('Выберите номер полки от 1 до 3, где будет храниться документ: ')
    adding = {'type': add_type, 'number': add_number, 'name': add_name}
    # try:
    #   assert add_number_directories in ['1', '2', '3'], 'введен несуществующий номер полки'
    # except Exception as e:
    #   print(e)
    #   documents.append(adding)
    # print(documents)
    add_new = directories.copy()
    # print(add_new)

    for num_number_directories in add_new.keys():
        if add_number_directories == num_number_directories:
            documents.append(adding)
            # print(num_number_directories)

        # documents.append(adding)
    else:
        pass
        # print('Выбранный документ не добавлен')
        # break

    for add_directories in add_new.keys():
        # print(add_new.keys())
        if add_number_directories == add_directories:
            print('Номер добавлен на указанную полку:')
            new_number = add_new[add_directories]
            # print(new_number)
            new_number.append(add_number)
            print(add_new)
            # if add_number_directories in add_directories:
            #   add_new.append(add_number)
            #   print('Номер добавлен на полку')

            #   # print(f'Номер добавлен на полку: {add_new}')
            break
    else:
        print('Выбранный номер полки не существует')

        # break
    # print(documents)
    # print(add_new)


# add()

def all_name():
    for name_owner in documents:
        try:
            # for name_owner in documents:
            # if all_name_owner in name.values():
            print(name_owner['name'])
        except KeyError:
            print('У некоторых документов отсутствует имя владельца')


# all_name()


while True:
    user_input = input(
        '\n Введите пользовательскую программу: \n "р" - команда, которая спросит номер документа и выведет имя человека, \n которому он принадлежит; \n "s" - команда, которая спросит номер документа и выведет номер полки, на которой он находится; \n "l" - команда, которая выведет список всех документов; \n "a" - команда, которая добавит новый документ в каталог и в перечень полок, \n спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться; \n "n" - команда, которая выводит имена всех владельцев документов; \n "q" - команда, которая завершает работу программы. \n')
    if user_input == 'p':
        request_people()
    elif user_input == 's':
        number_shelf()
    elif user_input == 'l':
        list_documents()
    elif user_input == 'a':
        add()
    elif user_input == 'n':
        all_name()
    elif user_input == 'q':
        print('До свидания!')
        break

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться


#     if add_number_directories == add_directories[0]:
#       add_directories[1].append(add_number)
#       print(f'Номер добавлен на полку {add_new[0]}')
#       print(add_new)
#   # break
#     else:
#       print('Выбранный номер полки не существует')
#     # break
# # print(directories)
# add()


# for add_directories in directories.keys():
#   if add_number_directories != add_directories:
#     print('Выбранный номер полки не существует')
#     break


# if add_number_directories in add_directories:
#   print(add_number_directories)
# else:
#   print('Выбранный номер полки не существует')
#   break


#     else:
#       print('Введенные данные не существуют')
#       break
# request_people()


























