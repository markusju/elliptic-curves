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

# Public Key
public = (p, n, G, Q, curve1)

# Generating a Signature
print("Signature Generation")

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

signed_message = (m, r, s)
print(signed_message)


# Verifying a Signature
print("Signature Verification")
r = signed_message[1]
s = signed_message[2]
m = signed_message[0]

p = public[0]
n = public[1]
G = public[2]
Q = public[3]

e = m

w = Point.invert(s, n)

u1 = (e*w) % n
u2 = (r*w) % n

x = u1 * G + u2 * Q

print(x)



