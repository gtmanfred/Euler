#!/usr/bin/python
def Euler_102():
    with open('script/triangles.txt') as f:
        alist = list(x for x in f.read().split('\n')[1:-1])
    for i in alist:
        ilist = [int(x) for x in i.split(',')]
        a = ilist[:2]
        b = ilist[2:4]
        c = ilist[4:]
        slope1 = (a[1]-b[1])/(a[0]-b[0])
        slope2 = (b[1]-c[1])/(b[0]-c[0])
        slope3 = (c[1]-a[1])/(c[0]-a[0])
        sd1 = 1 if b[0]>a[0] else -1
        sd2 = 1 if c[0]>b[0] else -1
        sd3 = 1 if a[0]>c[0] else -1
        c1 = a[1]-slope1*a[0]
        c2 = b[1]-slope2*b[0]
        c3 = c[1]-slope3*c[0]
        return [a,b,c]

if __name__=='__main__':
    print(Euler_102())
