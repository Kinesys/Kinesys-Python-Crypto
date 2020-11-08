#Kinesys RSA 하스타드 암호화(n값과 c값이 3개씩 주어지며 e값이 작은 경우)
import gmpy2
gmpy2.get_context().precision = 4096
 
from binascii import unhexlify
from functools import reduce
from gmpy2 import root
import gmpy

EXPONENT =  "e data" #여기에 e Data입력
 
 
 
def chinese_remainder_theorem(items):
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n
 
    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        r, s, d = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m
 
    # Make sure we return the canonical solution.
    return result % N
 
 
def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0
 
    while b:
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
 
    return (lastx, lasty, a)
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
 
 
def get_value(filename):
    with open(filename) as f:
        value = f.readline()
    return int(value, 16)
 
if __name__ == '__main__':
    C1 = 
    C2 = 
    C3 = 
    ciphertexts = [C1, C2, C3]
 
    N1 = 
    N2 = 
    N3 = 
    modulus = [N1, N2, N3]
    
    C_M = [(c,m) for c,m in zip(ciphertexts, modulus)]
 
    C = chinese_remainder_theorem(C_M)
    M = int(root(C, 3))
 
    M = hex(M)[2:]
    print(unhexlify(M).decode('utf-8'))
