from fib import fib
from maths import ispan
def Euler_104():
    test = -1
    for i in fib():
        test+=1
        stri = str(i)
        if test<300000:continue
        elif test==300000:print('start')
        if ispan(int(stri[-1:-10:-1])) and ispan(int(stri[:9])):return test
        if test%10000==0:print(test//10000)

if __name__=='__main__':
    print(Euler_104())
