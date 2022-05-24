
"""
3) Определить функцию-генератор fib_generator(n), которая принимает количество элементов последовательности Фибоначчи и
 итерируется по элементам последовательности. например fib_generator(3) создаст итератор для 3 элементов
 последовательности 0 1 1
Чи́сла Фибона́ччи — элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
987, 1597, 2584, 4181, 6765, 10946, 17711, …, в которой первые два числа равны 0 и 1, а каждое последующее число равно
  сумме двух предыдущих чисел
Написать подобную ф-ю fib_list(n) которая возвращает список с элементами последовательности.
Вызов ф-и fib_list(3) вернет список [0, 1, 1]
"""


def fib_generator():
    pass


def fib_list(n: int):
    if type(n) != int:              # TODO catch the exception input not int
    # if not isinstance(n, int):
        raise ValueError('"n" must be int')
    if n <= 0:
        raise ValueError('"n" can\'t be <= 0')
    if n == 1:
        return [0]
    fib = [0, 1] + [0] * (n - 2)
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


n = int(input("Enter the amount of elements in the Fibonacci sequence: "))
gen = fib_list(n)

print(gen)
# for i in gen:
#     print(i, end=' ')
