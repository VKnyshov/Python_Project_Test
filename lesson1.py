# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 1231231 asdasdqij 123okjkj222 nlnjkn 23 fdfdg544'
# digits = ','.join([i for i in st if i.isdigit()])
# print(digits)


# # #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


# import re
# st = 'as 23 fdfdg544 asd123asd'
# num = re.findall(r'\d+', st)
# res = ', '.join(num)
# print(res)
#

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# result = [i.upper() for i in greeting]
# print(result)


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# res = [x**2 for x in range(0, 51) if x % 2 != 0]
# print(res)

# function
#
#???????????????????????????????????????????????????????????????????????????????????????????????? - створити функцію яка виводить ліст
# def print_list(lst):
#     print(lst)
# print_list([1, 2, 3])



# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_of_three(a, b, c):
#     maximum = max(a, b, c)
#     # print(maximum)
#     return maximum
#
# print(max_of_three(5, 10, 3))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_and_max(*args):
#     if not args:
#         print("No numbers provided.") #перевірка, чи є числа
#         return None # якщо чисел немає виводить none
#     largest = max(args)
#     smallest = min(args)
#     print(largest)
#     return smallest
# print(min_and_max(4, 7, 1, 9, 2))


# - створити функцію яка повертає найбільше число з ліста

# def max_from_list(lst):
#     return max(lst)
# print(max_from_list([4, 711, 122, 921, 2]))


# - створити функцію яка повертає найменьше число з ліста

# def min_from_list(lst):
#     return min(lst)
# print(min_from_list([4, 711, 122, 921, 2]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_of_list(lst):
#     return sum(lst)
# print(sum_of_list([1, 2, 5]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def average_of_list(lst):
#     if not lst:
#         return 0
#     return sum(lst) / len(lst)
#
# print(average_of_list([1, 2, 3]))


# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню


def find_min(lst):
    # Знайти мінімальне число в списку.
    return min(lst)


def remove_duplicates(lst):
    # Видалити всі дублікати з списку.
    return list(set(lst))


def replace_every_fourth(lst):
    # Замінити кожне 4-те значення на 'X'.
    return ['X' if (i + 1) % 4 == 0 else x for i, x in enumerate(lst)]


def print_empty_square(size):
    # вивести пустий квадрат зі стороною size.
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')


def multiplication_table():
    # Вивести таблицю множення за допомогою циклу while.
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(f'{i * j:4}', end=' ')
            j += 1
        print()
        i += 1


def menu():
    # Головне меню програми.
    while True:
        print("\nГоловне меню:")
        print("1. Робота зі списком")
        print("2. Пустий квадрат")
        print("3. Таблиця множення")
        print("4. Вихід")

        choice = input("Введіть номер пункту меню: ")

        if choice == '1':
            sub_menu()
        elif choice == '2':
            size = int(input("Введіть розмір сторони квадрата: "))
            print_empty_square(size)
        elif choice == '3':
            multiplication_table()
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


def sub_menu():
    # Підменю для роботи зі списком.
    lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    while True:
        print("\nПідменю роботи зі списком:")
        print("1. Знайти мінімальне число")
        print("2. Видалити всі дублікати")
        print("3. Замінити кожне 4-те значення на 'X'")
        print("4. Повернутися до головного меню")

        sub_choice = input("Введіть номер пункту підменю: ")

        if sub_choice == '1':
            print("Мінімальне число в списку:", find_min(lst))
        elif sub_choice == '2':
            print("Список без дублікатів:", remove_duplicates(lst))
        elif sub_choice == '3':
            print("Список після заміни кожного 4-го значення:", replace_every_fourth(lst))
        elif sub_choice == '4':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


# Запуск програми
menu()
