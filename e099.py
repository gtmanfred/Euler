from math import log10
with open('script/base_exp.txt') as f:
    alist = list(c for c in f.read().split('\n'))[1:-1]
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
