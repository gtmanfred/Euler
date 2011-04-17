def Euler_14(num=10**6):
    maxlen=1
    for i in range(num//2,num):
        a=chainlen(i)
        if a>maxlen:
            maxlen,j=a,i
        if i ==num//4*3:
            print(i)
    return j

def chainlen(num=13):
    length=1
    while num != 1:
        num=3*num+1 if num%2 else num//2
        length+=1
    return length

if __name__=='__main__':
    print(Euler_14())
