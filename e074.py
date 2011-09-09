from time import time
from script.memorize import memo1of2
from e034 import sumdigfacts
fact = [1,1,2,6,24,120,720,5040,40320,362880]
def e074(top = 10**6):
    count = 0
    mini = 1000
    for i in range(1,top):
        if i>mini:print(i/top,end='\r');mini+=1000
        if chain(i,[])==60:
            count+=1
    return count
@memo1of2
def chain(n,c = []):
   nxt = sumdigfacts(n)
   if nxt in c:return 1
   else:return 1+chain(nxt,c+[n])

def sepdigs(num):
    return [int(x) for x in str(num)]

def Euler_74(top = 10**6):
    count = 0
    for i in range(1,top):
        if i%10**4==0:print('i:',i//10**4)
        chain = 0
        num = i
        nset = set()
        while not num in nset:
            nset.add(num)
            num1 = [int(x) for x in str(num)]
            num = sum([fact[x] for x in num1])
        if len(nset)==60:count+=1
    return count


if __name__=='__main__':
    x = 1000000
    t = time()
    print(e074(x),time()-t)
    #print(Euler_74(x),time()-t)
