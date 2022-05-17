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
    """Multiplying fractions and returns a fraction"""

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
        self.num = num  # numerator
        self.den = den  # denominator
        self.conv_fraction()

    @property
    def num(self) -> int:
        """Return numerator"""
        return self.__num

    @property
    def den(self) -> int:
        """Return denominator"""
        return self.__den

    @den.setter
    def den(self, den) -> None:
        """Checks the value of the denominator and sets the attribute value"""
        if den == 0:
            raise Exception("Denominator can't be a zero")
        self.__den = den

    @num.setter
    def num(self, num) -> None:
        """Sets the attribute value"""
        self.__num = num

    @staticmethod
    def gcd(numer, denom) -> int:
        """Finds and returns the greatest common denominator"""
        res = numer % denom
        while res != 0:
            numer, denom = denom, res
            res = numer % denom
        return denom

    def conv_fraction(self) -> None:
        """Converts a fraction like 2/4 to 1/2"""
        nod = Fraction.gcd(self.num, self.den)
        self.num //= nod
        self.den //= nod

    # subtraction
    def __sub__(self, other_sub):
        """Subtracts fractions and returns a fraction"""
        if self.den != other_sub.den:
            new_num = self.num * other_sub.den - self.den * other_sub.num
            new_den = self.den * other_sub.den
            return Fraction(new_num, new_den)
        else:
            new_num = self.num - other_sub.num
            new_den = self.den
            return Fraction(new_num, new_den)

    # addition
    def __add__(self, other_add):
        """Adds fractions and returns a fraction"""
        if self.den != other_add.den:
            new_num = self.num * other_add.den + self.den * other_add.num
            new_den = self.den * other_add.den
            return Fraction(new_num, new_den)
        else:
            new_num = self.num + other_add.num
            new_den = self.den
            return Fraction(new_num, new_den)

    # multiplication
    def __mul__(self, other_mul):
        """Multiplying fractions and returns a fraction"""
        return Fraction(self.num * other_mul.num, self.den * other_mul.den)

    # division
    def __truediv__(self, other_div):
        """Dividing fractions and returns a fraction"""
        return Fraction(self.num * other_div.den, self.den * other_div.num)

    def __str__(self) -> str:
        """Return a string object"""
        return f"{self.num}/{self.den}"

    @classmethod
    def change_str(cls, str_fraction):
        """Changes string to fraction"""
        num, den = map(int, str_fraction.split('/'))
        return cls(num, den)


fr1 = Fraction(2, 3)

fr2 = Fraction.change_str('3/4')

sub = fr1 - fr2
add = fr1 + fr2
mul = fr1 * fr2
div = fr1 / fr2

print("\nFirst fraction:", fr1)
print("Second fraction:", fr2)
print("\nResult of subtracting fractions:", sub)
print("Result of adding fractions:", add)
print("Result of multiplying fractions:", mul)
print("Result of dividing fractions:", div)
print("\nResult subtracting fractions (mixin):", Fraction.sub(fr1, fr2))
print("Result adding fractions (mixin):", Fraction.add(fr1, fr2))
print("Result multiplying fractions (mixin):", FractionMixin.mul(fr1, fr2))
print("Result dividing fractions (mixin):", FractionMixin.div(fr1, fr2))
