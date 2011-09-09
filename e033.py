from fractions import Fraction as f
from functools import reduce
from operator import mul
def e033():
    alist = []
    for y in range(1,10):
        for z in range(y,10):
            x=float(9)*y*z/(10*y-z)
            if int(x) == x and y/z < 1 and x<10:
                #print(x, y, z, str(10*y+x)+'/'+str(z+10*x), str(y)+'/'+str(z))
                alist+=[f(y,z)]
    return str(reduce(mul,alist)).split('/')[1]
if __name__=='__main__':
    print(e033())
