"""
Задание 1
Создать класс дробь(Fraction), конструктор которого принимает целые числа (num, den  -  числитель(numerator),
 знаменатель(denominator) ).
Выполнить
Атрибуты числитель и знаменатель в классе сделать приватными. Доступ к атрибутам реализовать через свойства.
Переопределить методы __sub__, __add__, __mull__, __truediv__ для того, чтобы можно было выполнять соответствующие
математические действия  с объектами класса дробь.
(Вычитание, сложение, умножение и деление).
В миксине реализовать статические методы, для этих же операций(add, sub, mull, div).
Добавить в класс миксин.
Создать classmethod который из строки типа 'числитель/знаменатель' возвращает объект класса дробь.
Переопределить метод __str__, который при выводе объекта на печать будет выводить строку вида num / den.
Создать объекты класса дробь.
Выполнить все реализованные методы.
"""


class Fraction:

    # instantiation
    def __init__(self, num: int, den: int) -> None:
        self.__num = num  # numerator
        self.__den = den  # denominator

    # subtraction
    def __sub__(self, other_sub):
        if self.__num == other_sub.__num:       # TODO не выполняется проверка равенства знаменателей
            new_num = self.__num * other_sub.__den - self.__den * other_sub.__num
            new_den = self.__den * other_sub.__den
            return Fraction(new_num, new_den)
        else:
            new_num = self.__num - other_sub.__num
            new_den = self.__den
            return Fraction(new_num, new_den)

    # addition
    def __add__(self, other_add):
        if self.__den == other_add.__den:    # TODO не выполняется проверка равенства знаменателей
            new_num = self.__num * other_add.__den + self.__den * other_add.__num
            new_den = self.__den * other_add.__den
            return Fraction(new_num, new_den)
        if self.__den != other_add.__den:
            new_num = self.__num + other_add.__num
            new_den = self.__den
            return Fraction(new_num, new_den)

    # multiplication
    def __mul__(self, other_mul):
        return Fraction(self.__num * other_mul.__num, self.__den * other_mul.__den)

    # division
    def __truediv__(self, other_div):
        return Fraction(self.__num * other_div.__den, self.__den * other_div.__num)

    def __str__(self) -> str:
        return f"{self.__num}/{self.__den}"
        # return str(self.__num) + "/" + str(self.__den)


p1 = Fraction(1, 2)

p2 = Fraction(2, 2)

sub = p1 - p2
add = p1 + p2
mul = p1 * p2
div = p1 / p2

print("\nFirst fraction:", p1)
print("Second fraction:", p2, "\n")
print("Result of subtracting fractions:", sub, "\n")
print("Result of adding fractions:", add, "\n")
print("Result of multiplying fractions:", mul, "\n")
print("Result of dividing fractions:", div)
# print()
