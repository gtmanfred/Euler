from math import sqrt
def Euler_64(top = 10**4):
    count = 0
    for i in range(0,top+1):
        if period(i)%2:count+=1
    return count

def period(num):
    tmp = limit = int(sqrt(num))
    if limit**2==num:return 0
    k, period = 1, 0
    while k !=1 or period == 0:
        k = (num - tmp * tmp) // k
        tmp = ((limit + tmp) // k) * k - tmp
        period += 1
    return period

if __name__=='__main__':
    print(Euler_64())
