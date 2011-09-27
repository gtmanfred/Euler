from script.maths import ncr
def e106(n=12):
    tot = 0
    for k in range(n//2+1):
        x = 2*k
        y = k+1
        if y>x or x==y:continue
        tot+=ncr(n,x)*ncr(x-1,y)
    return tot
if __name__=='__main__':
    print(e106(4))
    print(e106())
