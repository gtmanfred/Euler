from math import log10
alist = list(c for c in open('base_exp.txt').read().split('\n'))
def Euler_99():
    maxi = 0
    maxval = 0
    for i in range(len(alist)):
        pair = [int(x) for x in alist[i].split(',')]
        val = pair[1]*log10(pair[0])
        if val>maxval:maxval=val;maxi=i
    return (maxi+1)

if __name__=='__main__':
    print(Euler_99())
