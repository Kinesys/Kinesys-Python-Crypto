#Kinesys RSA d값 구하기.py
#p, q, c, e 값이 주어졌을 경우
import gmpy2

p = 
q =
e =
c =

n = p * q

phi = (p-1) * (q-1)

d = invert(e, phi)

print('%x' %pow(c, d, n)).decode("hex")
