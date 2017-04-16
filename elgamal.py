from curve import Curve, Point


p = 3077783
curve1 = Curve(65, -65, p)
G = Point(1, 1, curve1)

# Message (!Must be a point on the curve...!)
"""
You need a public known function f : m ↦ Pm which maps messages m to points Pm on E.
It should be invertible, and one way is to use m in the curve's equation as x and calculate the according y.
"""
M = Point(1154, 3038580, curve1)
print("M", M)

# Generating Public/Private Key
a = 34
Y = a*G
print("Y", Y)

public = (Y, G, p, curve1)
private = (a)


# Encrypting
Y = public[0]
G = public[1]
p = public[2]

k = 12
C = k*G
print("C", C)

D = M + k*Y
print("D", D)

enc_message = (C, D)

# Decrypting
a = private
recv_message = enc_message
C = recv_message[0]
D = recv_message[1]

# M = a*C - D
M_dec = D - a*C

print(M_dec)