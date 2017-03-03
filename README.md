# elliptic-curves - A basic implementation of elliptic curves in Python

This is a very basic implementation of elliptic curves in Python.
It allows to define a Curve(a, b, p) with 

E: y^2 = x^3 + a*x + b mod p


The point class allows to operate on this curve and implements addition and multiplication.

We provide several examples to demonstrate our implementation:
* ECDH (Diffie-Hellman)
* ECDSA (DSA)
* EC-Elgamal
