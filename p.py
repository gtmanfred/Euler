from maths import gcd
from memorize import memo
@memo
def a(n):
    if n==1:return 7
    else:
        return a(n-1)+gcd(n,a(n-1))
