check ='123456789'
from math import sqrt
def Euler_206():
    for i in range(138902662,101010101,-1): 
        last = i%10
        if last==3 or last==7:
            num = str(i*i)
            test = [num[x] for x in range(0,len(num),2)]
            checknum = ''.join(test)
            if checknum==check:return i*10


if __name__=='__main__':
    print(Euler_206())
