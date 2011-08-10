from numbertheory import phi
from allsieve import soe as sieve
def test(c=25,n = 4*10**7):
    plist = phi(n)
    print('pdone')
    count = 0
    for i in sieve(4*10**7):
        j = i
        chain = 1
        while chain<=25 and j!=1:
            j = plist[j]
            chain+=1
        if chain==25:count+=i
    return count
print(test())
