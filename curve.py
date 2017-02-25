"""
This is a very basic implementation of elliptic curves in Python.
It allows to define a Curve(a, b, p) with E: y^2 = x^3 + a*x + b mod p
The point class allows to operate on this curve and implements addition and multiplication.

A Curve may be defined as follows:

curve = Curve(1, 1, 5)

Points on the curve are initialized with a reference to a Curve object

p1 = Point(2, 1, curve)
p2 = Point(4, 3, curve)

The multiplication and addition operators for Points have been implemented, allowing to easily peform addition and scalar-multiplication:


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

    def get_points(self):
        list = []
        for x in range(0, self.p):
            y2 = (pow(x, 3) + self.a*x + self.b) % self.p
            y = pow(y2, 0.5)
            if not y.is_integer() or y2 == 0:
                continue
            y = int(y)
            list.append(Point(x, y%self.p, self))
            if not list[-1].is_infinity():
                list.append(Point(x, -y%self.p, self))
        #list.append(Point(0,0,self))
        return list


class Point:
    def __init__(self, x, y, curve):
        self.x = x % curve.p
        self.y = y % curve.p
        self.curve = curve

    @staticmethod
    def invert(x, p):
        return pow(x, p-2, p)

    def is_infinity(self):
        return self.x <= 0 and self.y <= 0

    def get_negative(self):
        return Point(self.x, -self.y%self.curve.p, self.curve)

    def get_order(self):
        res = Point(1, 1, self.curve)
        order = 1
        while not res.is_infinity():
            res = order*self
            order += 1
        return order

    def __repr__(self):
        return ""+self.__str__()

    def __str__(self):
        if self.is_infinity():
            return "(0)"
        return "("+str(self.x)+", "+str(self.y)+")"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("unsup")
        spoint = Point(0, 0, self.curve)
        for i in range(1, other+1):
            spoint += self
        return spoint

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("unsup")

        p1 = self
        p2 = other
        curve = self.curve

        #p1 is zero
        if p1.is_infinity():
            return p2
        #p2 is zero
        if p2.is_infinity():
            return p1

        # P1=-P2
        if p1.x == p2.x and p1.y == -p2.y % curve.p:
            return Point(0, 0, curve)

        #Slope m of g(x) = m*x + d
        if p1 == p2:
            m = (3*p1.x*p1.x+curve.a) * Point.invert(2*p1.y, curve.p)
        else:
            m = (p2.y-p1.y) * Point.invert(p2.x-p1.x, curve.p)

        m = m % curve.p
        d = (p1.y - m+p1.x) % curve.p


        #P3 = P1+P2
        x3 = (pow(m,2)-p1.x-p2.x) % curve.p
        y3 = (m*(p1.x-x3)-p1.y) % curve.p

        return Point(x3, y3, curve)
