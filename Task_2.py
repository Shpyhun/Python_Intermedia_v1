"""Создать класс Point2D. Координаты точки задаются 2 параметрами - координатами x, y на плоскости.
Реализовать метод distance который принимает экземпляр класса Point2D и рассчитывает расстояние между 2мя точками
на плоскости.
Создать защищенный атрибут класса - счетчик созданных экземпляров класса.
Чтение количества экземпляров реализовать через метод getter.
Создать класс Point3D, который является наследником класса Point2D. Координаты точки задаются 3 параметрами -
координатами x, y, z в пространстве.
Переопределить конструктор с помощью super().
Переопределить метод distance для определения расстояния между 2-мя точками в пространстве."""


class Point2D:

    __points_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.__points_count += 1

    @staticmethod
    def distance(point_1, point_2):
        return ((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2) ** 0.5

    @classmethod
    def point_count(cls):
        return cls.__points_count


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    @staticmethod
    def distance(point_3, point_4):
        return ((point_3.x - point_4.x) ** 2 + (point_3.y - point_4.y) ** 2 + (point_3.z - point_4.z)) ** 0.5


p1 = Point2D(10, 10)
print("\nCounter class instance:", Point2D.point_count())
p2 = Point2D(100, 100)

print("Distance between points on a plane:", round(Point2D.distance(p1, p2), 2))
print("Counter class instance:", Point2D.point_count())

p3 = Point3D(10, 10, 10)
print("Counter class instance:", Point2D.point_count())
p4 = Point3D(100, 100, 100)

print("Distance between points on a plane:", round(Point3D.distance(p3, p4), 2))
print("Counter class instance:", Point3D.point_count())
