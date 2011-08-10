def Euler_124(top = 1000):
    maxr = 0
    oldr = 0
    for a in range(2,top):
        if a%2:
            maxr+=a**2-a
        else:
            maxr+=a**2+2*a
    return maxr

if __name__=='__main__':
    print(Euler_124())
