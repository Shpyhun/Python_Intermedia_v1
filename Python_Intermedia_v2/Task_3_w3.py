
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


def fib_generator(n: int):
    """Iterates over the elements of a sequence Fibonacci"""
    num_fib_1 = 0
    num_fib_2 = 1
    if n <= 0:
        raise ValueError('"n" can\'t be <= 0')
    for i in range(n):
        yield num_fib_1
        num_fib_1, num_fib_2 = num_fib_2, num_fib_1 + num_fib_2


def fib_list(n: int) -> list:
    """Returns a list with the elements of a sequence Fibonacci"""
    if n <= 0:
        raise ValueError('"n" can\'t be <= 0')
    if n == 1:
        return [0]
    fib = [0, 1] + [0] * (n - 2)  # reserve memory
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


fib_gen = fib_generator(10)
gen_l = fib_list(10)

print("\nIterates over the elements of a sequence Fibonacci: ", end='')
for i in fib_gen:
    print(i, end=' ')
print("\n\nList with the elements of a sequence Fibonacci:", gen_l)
