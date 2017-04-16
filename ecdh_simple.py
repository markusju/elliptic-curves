from curve import Curve, Point

#ECDH - Elliptic Curve Diffie Hellman
curve1 = Curve(-1, 3, 7)
G = Point(2, 4, curve1)

#Alice
a = 5
kxa = a*G

#Bob
b = 2
kxb = b*G

# Key computation for Alice
ka = kxb*a
print(ka)

# Key computation for Bob
kb = kxa*b
print(kb)
