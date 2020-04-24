def enter_operation():
    input_op = input(
        "Введите один математический символ на выбор: '+', '-', '*', '/'  \nи два положительных числа через пробел, если хотите произвести математическую операцию: \n")
    # input_op = input_op.split(' ')

    input_sym = input_op.split()
    #   return (input_op)
    # Enter_operation()
    if len(input_sym) < 3:
        print('количество введенных данных меньше требуемого')
    elif len(input_sym) > 3:
        print('количество введенных данных больше требуемого')

    # number0 = input_sym[0]
    # number1 = int(input_sym[1])
    # number2 = int(input_sym[2])

    # if len(input_sym) != 3:
    # print('количество чисел не соответствует')
    # break
    # except IndexError:
    #   print('количество чисел не соответствует')

    try:
        number0 = input_sym[0]
        number1 = int(input_sym[1])
        number2 = int(input_sym[2])

        try:
            assert number0 in ['+', '-', '*', '/'], 'введен неправильный математический символ'
        except Exception as e:
            print(e)

        try:
            assert number1 >= 0 and number2 >= 0, 'введенное число меньше 0'
        except Exception as a:
            print(a)

        # assert number2 >= 0, 'введенное число меньше 0'

        # except:
        #   print('Проверьте правильность ввода!')

        # try:
        if number0 == '+':
            print(int(number1 + number2))
        elif number0 == '-':
            print(int(number1 - number2))
        elif number0 == '*':
            print(int(number1 * number2))
        elif number0 == '/':
            print(int(number1 / number2))
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
    except IndexError:
        print('Количество чисел не соответствует')
    except UnboundLocalError:
        print('Введите заново требуемый символ и добавьте числа')
    except ValueError:
        print('Операция строк и чисел невыполнима!')
    # except AssertionError:
    #   print('Введен неправильный математический символ')
    # if len(input_sym) != 3:
    #   print('количество чисел не соответствует1')
    # else:
    # pass


enter_operation()

#   try:
#     if input_op[1] > 0:
#       print('Число больше 0')
#   except ValueError:
#     # n != int
#     print("Что-то пошло не так")


# input_op = input_op.split(' ')
#     print(input_op)