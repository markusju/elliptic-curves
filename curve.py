from fractions import Fraction

"""
This is a very basic implementation of elliptic curves.
It allows to define a Curve(a, b, p) with E: y^2 = x^3 + a*x + b mod p
The point class allows to operate on this curve and implements addition and multiplication.

A Curve may be defined as follows:

curve = Curve(1, 1, 5)

p1 = Point(2, 1, curve)
p2 = Point(4, 3, curve)

p3 = p1+p2
p4 = 2*p1

print(p3)
print(p4)


"""

class Curve:
    # y^2 = x^3 + a*x +b
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p


class Point:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve

    @staticmethod
    def fractionmodp(fraction, p):
        return (fraction.numerator * pow(fraction.denominator, p-2, p)) % p

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")";

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("unsup")
        spoint = self
        for i in range(1, other+1):
            spoint +=spoint
        return spoint

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("unsup")

        p1 = self
        p2 = other
        curve = self.curve

        #Slope m of g(x) = m*x + d
        if p1 == p2:
            m = Fraction((3*pow(p1.x,2)+curve.a),2*p1.y)
        else:
            m = Fraction((p2.y-p1.y), (p2.x-p1.x))

        m = Point.fractionmodp(m, curve.p)
        d = (p1.y - m+p1.x) % curve.p


        #P3 = P1+P2
        x3 = (pow(m,2)-p1.x-p2.x) % curve.p
        y3 = (m*(p1.x-x3)-p1.y) % curve.p

        return Point(x3, y3, curve)

curve1 = Curve(1, 1, 5)
p1 = Point(2, 1, curve1)
p2 = Point(4, 2, curve1)

p3 = p1+p2
p4 = 4*p1

print(p3)
print(p4)
