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


class FractionMixin:
    """Multipying fractions and returns a fraction"""

    @staticmethod
    def add(fraction_1, fraction_2):
        """Adds fractions and returns a fraction"""
        if fraction_1.den != fraction_2.den:
            num_add = fraction_1.num * fraction_2.den + fraction_1.den * fraction_2.num
            den_add = fraction_1.den * fraction_2.den
            return Fraction(num_add, den_add)
        else:
            num_add = fraction_1.num + fraction_2.num
            den_add = fraction_1.den
            return Fraction(num_add, den_add)

    @staticmethod
    def sub(fraction_1, fraction_2):
        """Subtracts fractions and returns a fraction"""
        if fraction_1.den != fraction_2.den:
            num_sub = fraction_1.num * fraction_2.den - fraction_1.den * fraction_2.num
            den_sub = fraction_1.den * fraction_2.den
            return Fraction(num_sub, den_sub)
        else:
            num_sub = fraction_1.num - fraction_2.num
            den_sub = fraction_1.den
            return Fraction(num_sub, den_sub)

    @staticmethod
    def mul(fraction_1, fraction_2):
        """Multiplying fractions and returns a fraction"""
        return Fraction(fraction_1.num * fraction_2.num, fraction_1.den * fraction_2.den)

    @staticmethod
    def div(fraction_1, fraction_2):
        """Divides fractions and returns a fraction"""
        return Fraction(fraction_1.num * fraction_2.den, fraction_1.den * fraction_2.num)


class Fraction(FractionMixin):

    # instantiation
    def __init__(self, num: int, den: int) -> None:
        self.__num = num  # numerator
        self.den = den  # denominator

    @property
    def num(self) -> int:
        """Return int"""
        return self.__num

    @property
    def den(self) -> int:
        """Return int"""
        return self.__den

    @den.setter
    def den(self, den) -> None:
        if den == 0:
            raise Exception("Denominator can't be a zero")
        self.__den = den

    # subtraction
    def __sub__(self, other_sub):
        """Subtracts fractions and returns a fraction"""
        if self.den != other_sub.den:
            new_num = self.__num * other_sub.den - self.den * other_sub.__num
            new_den = self.den * other_sub.den
            return Fraction(new_num, new_den)
        else:
            new_num = self.__num - other_sub.__num
            new_den = self.den
            return Fraction(new_num, new_den)

    # addition
    def __add__(self, other_add):
        """Adds fractions and returns a fraction"""
        if self.den != other_add.den:
            new_num = self.__num * other_add.den + self.den * other_add.__num
            new_den = self.den * other_add.den
            return Fraction(new_num, new_den)
        else:
            new_num = self.__num + other_add.__num
            new_den = self.den
            return Fraction(new_num, new_den)

    # multiplication
    def __mul__(self, other_mul):
        """Multiplays fractions and returns a fraction"""
        return Fraction(self.__num * other_mul.__num, self.den * other_mul.den)

    # division
    def __truediv__(self, other_div):
        """Dividing fractions and returns a fraction"""
        return Fraction(self.__num * other_div.den, self.den * other_div.__num)

    def __str__(self) -> str:
        return f"{self.__num}/{self.den}"

    @classmethod
    def change_str(cls, str_fraction):
        """Change string to fraction"""
        num, den = map(int, str_fraction.split('/'))
        return cls(num, den)


fr1 = Fraction(1, 2)

fr2 = Fraction.change_str('2/3')

sub = fr1 - fr2
add = fr1 + fr2
mul = fr1 * fr2
div = fr1 / fr2

print("\nFirst fraction:", fr1)
print("Second fraction:", fr2)
print("Result of subtracting fractions:", sub)
print("Result of adding fractions:", add)
print("Result of multiplying fractions:", mul)
print("Result of dividing fractions:", div)
print("Result subtracting fractions (mixin):", Fraction.sub(fr1, fr2))
print("Result adding fractions (mixin):", Fraction.add(fr1, fr2))
print("Result multiplying fractions (mixin):", FractionMixin.mul(fr1, fr2))
print("Result dividing fractions (mixin):", FractionMixin.div(fr1, fr2))
