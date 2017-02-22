# elliptic-curves - A basic implementation of elliptic curves in Python

This is a very basic iplementation of elliptic curves.
It allows to define a Curve(a, b, p) with E: y^2 = x^3 + a*x + b mod p

The point class allows to operate on this curve and implements addition and multiplication.
A Curve may be defined as follows:

curve = Curve(1, 1, 5)

Whereas the points on the curve are referenced to the Curve object:

p1 = Point(2, 1, curve)
p2 = Point(4, 3, curve)

p3 = p1+p2
p4 = 2*p1

The Addition and Multiplication operators have been overriddden to provide native support of these operations on the points of the curve.

