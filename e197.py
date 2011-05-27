from math import floor
from memorize import memo
test = lambda x: int(2**(30.403243784-x**2))*10**(-9)
def e197(top = 10**12):
    i = 0
    while abs(rec(i)-rec(i+2))>10**-10:
        i+=1
    return rec(i)+rec(i+1)
@memo
def rec(n):
    if n ==0:return -1
    else:return test(rec(n-1))
if __name__=='__main__':
    print(e197())
