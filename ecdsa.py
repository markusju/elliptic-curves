from curve import Curve, Point

#ECDSA Implementation...

def hash(m):
    return m

m = 1512

p = 3077783
n = 3078653


curve1 = Curve(65, -65, p)
G = Point(1, 1, curve1)


# Private Key
d = 654321
Q = d * G
print("Q=", Q)

# Pseudorandom k with 1 <= k <= n-1
k = 1234567

#Compute k*G = (x, y)
kG = k*G
print("kG", kG)
r = kG.x

# 1/k mod n
k_inverse_n = Point.invert(k, n) % n

# Hash
e = hash(m)

# Signature
s = (k_inverse_n * (e + d*r)) % n

print(m, r, s)