#Kinesys 위너 공격(e값이 매우 큰 경우 가능한 공격).py
#n, e, c가 주어졌다고 가정

import ContinuedFractions
import Arithmetic
import RSAvulnerableKeyGenerator
import gmpy2
import gmpy

def hack_RSA(e, n):
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)

    for(k, d) in convergents:

        if k!= 0 and (e*d-1) %k == 0:
            phi = (e*d-1) // k
            s = n - phi + 1

            discr = s*s - 4*n

            if(discr  >= 0):
                t = Arithmetic.is_perfect_square(discr)

                if t != -1 and (s+t) %2 == 0:
                    print("Hacked")
                    return d

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5

    while(times > 0):
        e, n, d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e, n) is (", e, ",", n, ")")
        print("d = ", d)
        hacked_d = hack_RSA(e, n)

        if d == hacked_d:
            print("Hack Worked")
        else:
            print("Hack Failed")
        
        print("d = ", d, ", hacked_d = ", hacked_d)

        print("-----------------------------------------")

        times -= 1

        if __name__ = "--main":

            n =
            e = 
            c = 
            d = hack_RSA(e, n)

            print('%x' %pow(c, d, n)).decode("hex")


