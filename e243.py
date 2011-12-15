from fractions import Fraction as f
def getnumer(x):
    return int(str(x).split('/')[0])
def test(top=12):
    res = 0
    for x in range(1,top):
        if x == getnumer(f(x,top)):
            res+=1
    return res/(top-1)
if __name__=='__main__':
    start =892371480
    while 1:
        if test(start)<15499/94744:
            break
        print(start)
        start+=1
    print(start)
