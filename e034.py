from script.maths import factrec
from functools import reduce
#from operator import 

def Euler_34():
    ret = 0
    for i in range(3, 100000):
        if i ==sumdigfacts(i):
            print(i)
            ret+=i
    return ret


def sumdigfacts(num):
    return sum([factrec(int(i)) for i in str(num)])

if __name__=='__main__':
    print(Euler_34())
