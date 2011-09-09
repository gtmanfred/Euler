from script.fib import fib
from script.maths import ispan
def Euler_104():
    test = -1
    mini = 10**3
    for i in fib():
        test+=1
        stri = str(i)
        if test<300000:continue
        elif test==300000:print('start')
        if ispan(int(stri[-1:-10:-1])) and ispan(int(stri[:9])):return test
        if test>mini==0:print(test//10000);mini+=10**3

if __name__=='__main__':
    print(Euler_104())
