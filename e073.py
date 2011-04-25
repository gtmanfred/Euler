half =1/2 
third = 1/3
def Euler_73(den = 12000):
    count = set()
    for d in range(1,den+1):
        if d%120==0:print(d//120)
        for n in range(d//3-1,d//2+1):
            frac = n/d
            if frac>third and frac<half:
                count.add(frac)
            if frac>half:break
    return len(count)

if __name__=='__main__':
    print(Euler_73())
