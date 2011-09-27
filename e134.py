from script.allsieve import soe
def e134():
    top = 10**6
    bot = 5
    tot = 0
    primes = soe(top+1)
    primes = primes[primes.index(bot):]
    mini = 100;
    for i, num in enumerate(primes):
        if i>mini:
            print(i/len(primes))
            mini+=100
        if i==len(primes)-1:
            break
        tot += findnum(num, primes[i+1])
    return tot

def findnum(p1,p2):
    testp1 = str(p1)
    i = 1
    while 1:
        test = int(str(i)+testp1)
        if test%p2==0:
            return test
        else:
            i+=1

if __name__=='__main__':
    print(e134())
