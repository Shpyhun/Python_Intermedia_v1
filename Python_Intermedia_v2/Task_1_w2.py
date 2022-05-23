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


# Define own exception
class FormulaError(Exception):
    """An exception is thrown due to a formula input error"""
    pass


def calculator(form_str: str):
    """Returns the result of the operation"""
    form_str = form_str.split()
    if len(form_str) != 3:
        raise FormulaError("Formula entered incorrectly")
    try:
        form_str[0] = float(form_str[0])
        form_str[2] = float(form_str[2])
    except ValueError:                                      # TODO отловить ошибку ввода str
        print("Values entered incorrectly")
    except FormulaError:
        print("Values entry error")
    try:
        form_str[1] not in "+-*/"                           # TODO  отловить ошибку ввода оператора
    except ValueError:
        print("Formula entered incorrectly")
    else:
        if form_str[1] == "+":
            return form_str[0] + form_str[2]
        elif form_str[1] == "-":
            return form_str[0] - form_str[2]
        elif form_str[1] == "*":
            return form_str[0] * form_str[2]
        elif form_str[1] == "/":
            try:
                form_str[2] != 0
                return form_str[0] / form_str[2]
            except ZeroDivisionError:
                return "Divider can't be a zero"
    return form_str


calc = "1 / /1"

print(calculator(calc))
# print(str_num)
