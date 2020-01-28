# 예제 1-2 간단한 2차원 벡터 클래스

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, sclar):
        return Vector(self.x * scalar, self.y * scalar)

# 특별 메서드는 주로 파이썬 인터프리터가 호출


