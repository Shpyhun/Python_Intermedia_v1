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
        self.num = num    # numerator
        self.den = den    # denominator

    # subtraction
    def __sub__(self, other_sub):
        # if type(other_sub) == int:
        if type(other_sub) == type(self):
            if self.den == other_sub.den:
                new_num = self.num * other_sub.den - self.den * other_sub.num
                new_den = self.den * other_sub.den
                return Fraction(new_num, new_den)
            else:
                new_num = self.num - other_sub.num
                new_den = self.den
                return Fraction(new_num, new_den)
        raise TypeError('Must be int')

    # addition
    def __add__(self, other_add):
        if type(other_add) == type(self):
            if self.den == other_add.den:
                new_num = self.num*other_add.den + self.den*other_add.num
                new_den = self.den * other_add.den
                return Fraction(new_num, new_den)
            else:
                new_num = self.num + other_add.num
                new_den = self.den
                return Fraction(new_num, new_den)
        raise TypeError('Must be int')

    # multiplication
    def __mul__(self, other_mul):
        return Fraction(self.num * other_mul.num, self.den * other_mul.den)

    # division
    def __truediv__(self, other_div):
        return Fraction(self.num / other_div.num, self.den / other_div.den)


p1 = Fraction(2, 2)
p2 = Fraction(2, 5)

sub = p1 - p2
add = p1 + p2
mul = p1 + p2
div = p1 / p2


print(p1)
print(p2)
print(sub)
print(add)
print(mul)
print(div)
