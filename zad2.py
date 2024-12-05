import math

class Vector:
    def __init__(self, coordinates):
        self.coordinates = list(coordinates)

    def __repr__(self):
        return f"Vector({self.coordinates})"

    def __add__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь одинаковое количество координат")
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь одинаковое количество координат")
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def dot_product(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь одинаковое количество координат")
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def cosine_angle(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Векторы должны иметь одинаковое количество координат")
        return self.dot_product(other) / (self.norm() * other.norm())

    def norm(self):
        return math.sqrt(sum(a ** 2 for a in self.coordinates))

    def __mul__(self, scalar):
        return Vector([a * scalar for a in self.coordinates])

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Нельзя делить на ноль")
        return Vector([a / scalar for a in self.coordinates])
