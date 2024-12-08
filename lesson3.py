# Створити клас Rectangle. Він має приймати дві сторони x,y. Описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == перевырку площин на рівність
#   != перевырку площин на не рівність
#   >, <  перевырку на меньше, більше
#   при виклику метода len() підраховувати сумму сторін


class Rectangle:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def area(self):
    """Обчислення площі прямокутника."""
    return self.x * self.y

  def __add__(self, other):
    """Додавання площ двох прямокутників."""
    return self.area() + other.area()

  def __sub__(self, other):
    """Різниця площ двох прямокутників."""
    return self.area() - other.area()

  def __eq__(self, other):
    """Перевірка рівності площ."""
    return self.area() == other.area()

  def __ne__(self, other):
    """Перевірка нерівності площ."""
    return self.area() != other.area()

  def __lt__(self, other):
    """Перевірка, чи площа менша."""
    return self.area() < other.area()

  def __gt__(self, other):
    """Перевірка, чи площа більша."""
    return self.area() > other.area()

  def __len__(self):
    """Повернення суми сторін."""
    return self.x + self.y


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 8)

print(f"Площа прямокутника 1: {rect1.area()}")  # 20
print(f"Площа прямокутника 2: {rect2.area()}")  # 18
print(f"Сума площ: {rect1 + rect2}")  # 38
print(f"Різниця площ: {rect1 - rect2}")  # 2
print(f"Рівність площ: {rect1 == rect2}")  # False
print(f"Нерівність площ: {rect1 != rect2}")  # True
print(f"rect1 > rect2: {rect1 > rect2}")  # True
print(f"rect1 < rect2: {rect1 < rect2}")  # False
print(f"Сума сторін rect1: {len(rect1)}")  # 9
print(f"Сума сторін rect2: {len(rect2)}")  # 9


print('*' * 200)

# ###############################################################################
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age


class Cinderella(Human):
  count = 0  # Змінна класу для підрахунку екземплярів

  def __init__(self, name, age, shoe_size):
    super().__init__(name, age)
    self.shoe_size = shoe_size
    Cinderella.count += 1  # Збільшуємо лічильник екземплярів

  @classmethod
  def get_count(cls):
    """Метод класу для отримання кількості створених екземплярів."""
    return cls.count


class Prince(Human):
  def __init__(self, name, age, found_shoe_size):
    super().__init__(name, age)
    self.found_shoe_size = found_shoe_size

  def find_cinderella(self, cinderellas):
    """Метод для пошуку попелюшки з відповідним розміром черевичка."""
    for cinderella in cinderellas:
      if cinderella.shoe_size == self.found_shoe_size:
        return cinderella
    return None


# Приклад використання
cinderella1 = Cinderella("Anna", 19, 38)
cinderella2 = Cinderella("Elsa", 22, 37)
cinderella3 = Cinderella("Maria", 18, 32)
prince = Prince("Philip", 25, 37)

# Список попелюшок
cinderellas = [cinderella1, cinderella2, cinderella3]

# Пошук попелюшки
found_cinderella = prince.find_cinderella(cinderellas)
if found_cinderella:
  print(f"Принц знайшов свою попелюшку: {found_cinderella.name}, {found_cinderella.age} років")
else:
  print("Принц не знайшов свою попелюшку.")

# Кількість створених попелюшок
print(f"Кількість створених попелюшок: {Cinderella.get_count()}")


print('*' * 200)


# ###############################################################################
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod

class Printable(ABC):
    """Абстрактний клас з абстрактним методом print."""
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    """Клас Book наслідується від Printable."""
    def __init__(self, name):
        self.name = name

    def print(self):
        """Реалізація абстрактного методу print."""
        print(f"Book: {self.name}")


class Magazine(Printable):
    """Клас Magazine наслідується від Printable."""
    def __init__(self, name):
        self.name = name

    def print(self):
        """Реалізація абстрактного методу print."""
        print(f"Magazine: {self.name}")


class Main:
    """Клас Main, який управляє списком printable_list."""
    printable_list = []

    @classmethod
    def add(cls, item):
        """Додає екземпляр до списку, якщо це Book або Magazine."""
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        """Виводить усі журнали."""
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        """Виводить усі книги."""
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

print("Magazines:")
Main.show_all_magazines()
print('-' * 40)

print("Books:")
Main.show_all_books()
print('*' * 200)
