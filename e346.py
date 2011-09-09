from script.memo import memo
from script.base import inBase
def test(top=10**12):
    s = 1
    b=2
    while (1+b+b**2<top):
        n = 1+b
        p = b*b
        while 1:
            n+=p
            if n>=top:
                break
            s+=n
            p*=b
        b+=1
    return s-31-8191

def e346(top=10**12):
    num='1'
    adict = {}
    while int(num,2)<=top:
        for b in range(2,36):
            tmp = int(num,b)
            if tmp>=top:break
            if adict.get(tmp):
                adict[tmp]=adict.get(tmp)+1
            else:
                adict[tmp]=1
        num+='1'
    ret = [i for i in adict.keys() if adict.get(i)>=2 or (adict.get(i)>=1 and\
        i>36)]
    return ret
if __name__=='__main__':
    print(test())
    #print(sum(e346(1000)))
