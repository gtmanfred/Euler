import maths
def Euler_35(num=10**6):
    primesdict = maths.primesd(num)
    primes = [x for x in primesdict.keys() if primesdict.get(x) is 1]
    tot = 0
    for x in primes:
        xstr = str(x)
        isp = 1
        for i in range(len(xstr)):
            xstr=rotatestr(xstr)
            if primesdict.get(int(xstr))==0:
                isp=0
                break
        if isp:tot+=1
    return tot

def rotatestr(num):
    if len(num)<2:
        return int(num)
    ret = num[1:]+num[0]
    return ret

if __name__=='__main__':
    print(Euler_35())
