from time import time
from maths import all_factors,primesd
t = time()
def e095(top=10**6):
    div = [0 for i in range(top)]
    for i in range(1,top):
        for j in range(2*i, top, i):
            div[j] += i
    maxdict={}
    testdict = {}
    for i in range(len(div)):
        tmp = div[i]
        if testdict.get(i):continue
        adict={div[i]:1}
        testdict[i]=1
        testdict[tmp]=1
        while True:
            try:tmp = div[tmp]
            except:break
            testdict[tmp]=1
            if tmp>top:break
            elif tmp==div[i]:
                if len(adict)>len(maxdict):
                    maxdict = adict
                    print('i:',min(maxdict),' max:',len(maxdict),' time:',time()-t)
                    print(maxdict)
                break
            elif adict.get(tmp):break
            else:adict[tmp]=1
        if i ==12496:print(i)
    return min(maxdict)
            

def e095_slow(top = 10**6):
    p = primesd(top)
    maxdict = {}
    aset = set()
    for i in range(2,top):
        if i%10**3==0:print(i,time()-t)
        if p.get(i):continue
        adict = {}
        tmp = i
        while True:
            tmp = sum(all_factors(tmp))-tmp
            if p.get(tmp) or tmp>=top:break
            elif adict.get(tmp):break
            elif tmp==i:
                adict[i] = 1
                if len(adict)>len(maxdict):
                    maxdict = adict
                    print('i:',i,' max:',len(maxdict),' time:',time()-t)
                    print(maxdict)
                break
            else:adict[tmp]=1
        if i ==14316:print(i)
    return min(maxdict.keys())
            

if __name__=='__main__':
    print(e095())
