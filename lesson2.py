# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання

from typing import Callable, List, Tuple


def notebook() -> Tuple[Callable[[str], None], Callable[[], List[str]]]:
    todo_list: List[str] = []  # Типізація списку рядків

    def add_todo(todo: str) -> None:
        todo_list.append(todo) #Додає нову справу до списку

    def get_all() -> List[str]:
        return todo_list.copy() #Повертає всі справи.

    return add_todo, get_all  # Повертаємо обидві функції як кортеж

add_todo, get_all = notebook()

add_todo("Хліб")
add_todo("Навчання")
add_todo("Приготувати вечерю")
add_todo("Пробіжка")
add_todo("Купити молоток")

print(get_all())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
from typing import List

def expanded_form(num: int) -> str: #Повертає число у вигляді суми розрядів.
    digits: List[str] = []  # Список для збереження розрядів у вигляді рядків
    num_str: str = str(num)  # Перетворюємо число на рядок для ітерації
    length: int = len(num_str)  # Довжина числа

    for i, digit in enumerate(num_str):
        if digit != '0':  # Пропускаємо нулі
            zeros: int = length - i - 1  # Кількість нулів після цифри
            digits.append(digit + '0' * zeros)  # Формуємо розряд

    return ' + '.join(digits)  # З'єднуємо розряди у рядок із роздільником " + "

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

# @decor
# def fun1():
#     print('func1')
#
# @decor
# def fun2():
#     print('func2')
#
# fun1()
# fun1()
# fun2()
# fun1()
############################################
from typing import Callable, Dict

def decor(func: Callable) -> Callable: #Декоратор для підрахунку викликів функції.
    call_count: Dict[str, int] = {}  # Словник для збереження кількості викликів

    def wrapper(*args, **kwargs):
        func_name = func.__name__  # Ім'я функції
        call_count[func_name] = call_count.get(func_name, 0) + 1  # Збільшуємо лічильник
        result = func(*args, **kwargs)  # Викликаємо оригінальну функцію
        print(f"*****'{func_name}' ***** {call_count[func_name]} раз(и)*****")
        return result

    return wrapper

@decor
def fun1():
    # print('func1')
    pass
@decor
def fun2():
    # print('func2')
    pass
fun1()
fun1()

print('Вася')

fun2()
fun1()
