from decimal import *
x = [x for x in range(1,101)]
squares = dict.fromkeys(x,1)
for i in range(1,11):
    squares[i**2]=0
def Euler_80():
    sums = 0
    for i in squares.keys():
        if squares.get(i):
            j = 1
            for sqrt in root(i):
                if j>100:break
                sums += sqrt
                j+=1
    return(sums)

def root(num):
    getcontext().prec = 200
    num =list(str(Decimal(num).sqrt()))
    del num[num.index('.')]
    i = 0
    while i<len(num):
        if num[i]=='.':i = i+1
        dig = int(num[i])
        yield dig
        i+=1

if __name__=='__main__':
    print(Euler_80())
