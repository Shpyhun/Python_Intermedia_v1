"""
1) Необходимо написать функцию калькулятор, которая принимает строку состоящую из числа, оператора и второго числа
разделенных пробелом. Например ('1 + 1'); Необходимо разделить строку используя str.split(), и проверить является
результирующий список валидным.

a) Если ввод не состоит из 3 элементов, необходимо возбудить исключение FormulaError, которое является пользовательским
 исключением.

b) Попытайтесь сконвертировать первое и третье значение ввода к типу float. Перехватите любые исключения типа
ValueError, которые возникают, и выбросите FormulaError

c) Если второе значение ввода не является '+', '-', '*', '/' также выбросите FormulaError.

Если инпут валидный - ф-я должна вернуть результат операции
"""


def calculator(str_calc: str):
    if len(str_calc.split()) != 3:
        return "FormulaError"
    num_1, oper, num_2 = str_calc.split()
    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        return "FormulaError"
    if oper not in "+-*/":
        return "FormulaError"

    # if num_2 == None:
    return num_1, oper, num_2



calc = "11 + 22"

print(calculator(calc))