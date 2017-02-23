from curve import Curve, Point

curve1 = Curve(65, -65, 3077783)
p1 = Point(4, 2, curve1)
p2 = 9*p1


#ECDH - Elliptic Curve Diffie Hellman
G = Point(1, 1, curve1)

#Alice
a = 43
kxa = a*G

#Bob
b = 12
kxb = b*G

# Key computation for Alice
ka = kxb*a
print(ka)

# Key computation for Bob
kb = kxa*b
print(kb)
