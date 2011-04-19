def Euler_39(num = 1000):
    ret= 0
    maxp = 0
    for p in range(12,num+1):
        sol = 0
        #a<b<c
        for a in range(1,p//3):
            for b in range(a,(p-a)//2):
                c = p-a-b
                if a**2+b**2==c**2:sol +=1
        if sol>maxp:
            maxp = sol
            ret = p

    print(maxp)
    print(ret)
    return ret

if __name__=='__main__':
    print(Euler_39())
