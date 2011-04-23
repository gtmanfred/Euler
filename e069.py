from maths import primes
primes = primes(200)
print(primes)
def Euler_69():
    maxp = 1
    for i in primes:
        if i*maxp>1000000:return maxp
        maxp*=i

if __name__=='__main__':
    print(Euler_69())
