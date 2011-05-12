from maths import primes
def e123(top=pow(10,10)): 
    p = primes(1000000)
    for n in range(len(p)):
        if ((2*(n+1)*p[n])%(p[n]*p[n]) > top and n%2 == 0):
            return n+1
if __name__=='__main__':
    print(e123(4))
    print(e123(pow(10,9)))
