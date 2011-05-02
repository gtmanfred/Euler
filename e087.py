from maths import primesd2
maxp = 10**4
top = 50000000
def Euler_87():
    prime1 = primesd2(maxp)
    count = set()
    x = 1
    last = 0
    for i in primesd2(90):
        tmp =i**4
        if tmp>=top:break
        print(i)
        for j in primesd2(400):
            tmp=j**3+i**4
            if tmp>=top:break
            for k in primesd2(8000):
                tmp = k**2+j**3+i**4
                if tmp == top:print('wtf')
                if tmp<top:
                    count.add(tmp)
                else:break
    return len(count)
    '''
    for i in prime1:
        if i**4>top:break
        print(i)
        x +=1
        prime2 = primesd2(maxp)
        for j in prime2:
            if i**4+j**3>top:break
            prime3 = primesd2(maxp)
            for k in prime3:
                if i**4+j**3+k**2>top:break
                count+=1
    return count
    '''
if __name__=='__main__':
    print(Euler_87())
