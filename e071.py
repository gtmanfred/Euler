def Euler_71(maxn = 10**6):
    num =3/7 
    minn=num
    for i in range(maxn,maxn-10,-1):
        j = num - int(i*num) * 1.0/i
        if minn>j and j!=0:minn,D = j,i
    return int(num*D)

if __name__=='__main__':
    print(Euler_71())
