from random import randrange,seed
def e339(n = 10000,s=0):
    seed(s)
    test = True
    i = 1
    maxb = 0
    while i<10000:
        if i%10000==0:print(i)
        b = n
        w = n
        last = n
        x = 2*n
        while True:
            r = randrange(b+w)
            if r in list(range(b)):
                b+=1
                w-=1
            else:
                b-=1
                w+=1
            if b+w>x:b = x-w
            if b<last:
                if b==w:w-=1
                elif b<w:
                    if b==1:w = 0
                    else:w = b-1
            x = b+w
            if b<=0 or w<=0:break
            last = b
        i+=1
        if b>=x:b = x
        maxb+=b
    return maxb/i

if __name__=='__main__':
    mins = 1 
    for s in range(101):
        print(s)
        a = e339(5,s)
        if abs(6.871346-a<mins):mins = 6.8771346-a;t=s
    print(mins,t)
