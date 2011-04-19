import maths
primesd = maths.primesd(10**6)
primes = [x for x in primesd.keys() if primesd.get(x) is 1]
def Euler_50():
    high = 0
    print(len(primes))
    for i in range(10):
        sums = 0
        x = 0
        if i%10000==0:
            print('new',i)
        for j in primes[i:]:
            x+=1
            sums +=j
            if sums>10**6:break
            if primesd.get(sums):
                if x>high:high = x; maxs =sums;print('high:',high,'sum:',sums,'i:',primes[i])
    return maxs


if __name__=='__main__':
    print(Euler_50())
