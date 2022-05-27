"""1) Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и
сохранять их в таком виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и
имя целевого файла. Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела,
после чего должен идти текст строки из исходного файла.
"""


def read_file():
    try:
        # file = open(input("Input name file: "), encoding='utf-8')
        file = open('1.txt', encoding='utf-8')
        new_file = open(input("Input name new file: "), 'w', encoding='utf-8')
        file.readline()
    except TypeError:
        raise "Error name file"
    # except FileNotFoundError:
    #     raise "Error name file"
    finally:
        file.close()
        new_file.close()


read_file()
