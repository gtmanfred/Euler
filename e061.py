def e061():
    tri = lambda n:n*(n+1)//2
    sqr = lambda n:n**2
    pent = lambda n:n*(3*n-1)//2
    hexa = lambda n:n*(2*n-1)
    hept = lambda n:n*(5*n-3)//2
    octa = lambda n:n*(3*n-2)
    tris = retlist(tri)
    sqrs = retlist(sqr)
    pents = retlist(pent)
    hexas = retlist(hexa)
    hepts = retlist(hept)
    octas = retlist(octa)
    test = [sqrs,pents,hexas,hepts,octas]
    for a in tris:
        for i,b in 

def retlist(f):
    alist = [0]
    i = 0
    while alist[-1]<10**4:
        i+=1
        alist+=[f(i)]
    return alist
if __name__=='__main__':
    print(e061())
