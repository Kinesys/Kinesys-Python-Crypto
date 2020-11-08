#Kinesys RSA p, q값이 비슷할 경우 n 값으로 p, q값 구하기.py
##n, e, c 값이 주어졌다고 가정

from gmpy2 import *

n =

e =

c =

p = isqrt(n)

while True:
    q, r = t_divmod(n, p)
    
    if r == 0:
        break
    p += 1

phi = (p-1) * (q-1)

d = invert(e, phi)

print ('%x' %pow(c,d,n)).decode("hex")
