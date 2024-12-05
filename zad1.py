import math

class ComplexNumber:
    def __init__(self, real=0, imag=0, *, polar=False, magnitude=0, angle=0):
        if polar:
            # в полярной форме инициализ
            self.real = magnitude * math.cos(angle)
            self.imag = magnitude * math.sin(angle)
        else:
            # алгебраич форме инициализ
            self.real = real
            self.imag = imag

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

    @property
    def magnitude(self):
        return math.sqrt(self.real**2 + self.imag**2)

    @property
    def angle(self):
        return math.atan2(self.imag, self.real)

    def to_polar(self):
        return self.magnitude, self.angle

    def to_algebraic(self):
        return self.real, self.imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        magnitude = self.magnitude * other.magnitude
        angle = self.angle + other.angle
        return ComplexNumber(polar=True, magnitude=magnitude, angle=angle)

    def __truediv__(self, other):
        magnitude = self.magnitude / other.magnitude
        angle = self.angle - other.angle
        return ComplexNumber(polar=True, magnitude=magnitude, angle=angle)

'''
# делаем в алгебраической 
z1 = ComplexNumber(real=3, imag=4)
print("Алгебраическая форма z1:", z1)
print("Полярная форма z1:", z1.to_polar())

# делаем полярную 
z2 = ComplexNumber(polar=True, magnitude=5, angle=math.pi / 4)
print("Алгебраическая форма z2:", z2)
print("Полярная форма z2:", z2.to_polar())

# смотрим теперь как тут операция тут 
z3 = z1 + z2
print("z1 + z2 =", z3)

z4 = z1 - z2
print("z1 - z2 =", z4)
z5 = z1 * z2
print("z1 * z2 =", z5)

z6 = z1 / z2
print("z1 / z2 =", z6)
'''