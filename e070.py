from script.maths import primesd2
def Euler_70():
    maxrat = 10
    prim1 = primesd2(10**7)
    p = [0]
    for i in prim1:
        if i**2>10**7:break
        if i>3:print(i)
        if p==[0]:
            prim2 = primesd2(10**7)
            p = []
        else:
            prim2 = p[p.index(i):]
        for j in prim2:
            p += [j]
            ij = i*j
            if ij>10**7:break
            if i ==j:
                phi = (i-1)*j
            elif i!=j:
                phi = (i-1)*(j-1)
            rat = ij/phi
            if sorted(str(ij))==sorted(str(phi)) and rat<maxrat:
                maxij = ij
                maxphi = phi
                maxrat = rat
                print('rat:',rat,'phi:',phi,'ij:',ij,'i:',i,'j:',j)
    return [maxrat,maxphi,maxij]


if __name__=='__main__':
    print(Euler_70())
