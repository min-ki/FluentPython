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
        """
        벡터의 크기가 0이면 False이고 아니면 True
        """
        return bool(abs(self))


    def __add__(self, other):
        """
        + 연산자
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, sclar):
        """
        * 연산자
        """
        return Vector(self.x * scalar, self.y * scalar)

# 특별 메서드는 주로 파이썬 인터프리터가 호출
# __repr__() 특별 메서드는 객체를 문자열로 표현
# __str__() 메서드는 str() 생성자에 의해 호출되며 print() 함수에 의해 암묵적 사용
# 둘중 하나만 구현해야 한다면 __repr__() 메서드를 구현하라.
# 파이썬 인터프리터는 __str__()이 없으면 __repr__() 메서드를 호출한다.

# 사용자 정의형의 불리언 값
# __bool__(), __len__()을 구현하지 않은 경우에는 사용자 정의 클래스의 객체는 참값으로 간주
# bool(x)는 x.__bool__()을 호출한 결과를 이용
# __bool__()이 없다면 파이썬은 x.__len__()을 호출하며, 이메소드가 0을 반환하면 bool()은 False를, 그렇지 않으면 True를 반환한다.


