#Kinesys RSA 낮은 지수 공격 (e값이 매우 작고 n값이 매우 큰 경우).py
#c, e값이 주어진 경우
#e가 3라고 가정한 코드(보통 e값은 3임)
from gmpy2 import *

c = #c data 입력

with local_context() as ctx:
    ctx.precision = 3000 #정밀도에 관한 값 만약 결과 값이 제대로 나오지 않으면 해당 값을 더 높게 수정한다.
    m = cbrt(c)

    print('%x' %int(m)).decode("hex")


