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

    def set_den(self):
        pass

    @property
    def num(self):
        return self.__num
        pass

    @property
    def den(self):
        return self.__den
        pass

    # subtraction
    def __sub__(self, other_sub):
        if self.__den != other_sub.__den:
            new_num = self.__num * other_sub.__den - self.__den * other_sub.__num
            new_den = self.__den * other_sub.__den
            return Fraction(new_num, new_den)
        else:
            new_num = self.__num - other_sub.__num
            new_den = self.__den
            return Fraction(new_num, new_den)

    # addition
    def __add__(self, other_add):
        if self.__den != other_add.__den:
            new_num = self.__num * other_add.__den + self.__den * other_add.__num
            new_den = self.__den * other_add.__den
            return Fraction(new_num, new_den)
        else:
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

    @classmethod
    def ret_fraction(cls, __num, __den):
        return cls(__num, __den)
        pass


class FractionMixin:

    @staticmethod
    def add(fr1, fr2):
        if fr1.den != fr2.den:
            newnum = fr1.num * fr2.den + fr1.den * fr2.num
            newden = fr1.den * fr2.den
            return Fraction(newnum, newden)
        else:
            newnum = fr1.num + fr2.num
            newden = fr1.den
            return Fraction(newnum, newden)

    @staticmethod
    def sub(fr1, fr2):              #TODO finalize the sub
        return Fraction()
        pass

    @staticmethod
    def mul(fr1, fr2):              #TODO finalize the mul
        return Fraction()
        pass

    @staticmethod
    def div(fr1, fr2):              #TODO finalize the div
        return Fraction()
        pass

fr1 = Fraction(1, 2)

fr2 = Fraction(1, 3)

sub = fr1 - fr2
add = fr1 + fr2
mul = fr1 * fr2
div = fr1 / fr2

print("\nFirst fraction:", fr1)
print("Second fraction:", fr2, "\n")
print("Result of subtracting fractions:", sub, "\n")
# print("Result of adding fractions:", add, "\n")
# print("Result of multiplying fractions:", mul, "\n")
# print("Result of dividing fractions:", div)
print("Result adding fractions (mixin):", FractionMixin.add(fr1, fr2))
