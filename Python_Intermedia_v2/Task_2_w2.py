"""
2) Определите класс итератор ReverseIter, который принимает список и итерируется по нему в обратном направлении
"""


class ReverseIter:

    def __init__(self, list_iter: list):
        self.list_iter = list_iter

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        if self.ind > len(self.list_iter) - 1:
            raise StopIteration
        else:
            elem = self.list_iter[-self.ind - 1]
            self.ind += 1
            return elem


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_for_iteration = ReverseIter(my_list)

print("\nList iteration in reverse: ", end='')

for elem in list_for_iteration:
    print(elem, end=', ')
