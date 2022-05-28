"""1) Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и
сохранять их в таком виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и
имя целевого файла. Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела,
после чего должен идти текст строки из исходного файла.
"""


def read_file():
    try:
        with open(input("Input name file: "), encoding='utf-8') as f:
            with open(input("Input name new file: "), 'a', encoding='utf-8') as nf:
                count = 0
                for row in f:
                    count += 1
                    nf.write(f'{count}: {row}')
    except FileNotFoundError:
        print('Error name file')
    except IOError:
        print('Something else')


read_file()
