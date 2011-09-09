from script import maths
import itertools

def Euler_41():
    high = [0]
    for i in range(1,8):
  #      primes = [str(x) for x in maths.primes(10**(i)//4,10**(i-1)//4)]
        alist =["".join(x) for x in  itertools.permutations("".join([str(x) for x in range(1,i+1)]))]
        high=[x for x in alist if maths.isprime2(int(x))]
    return high[-1]
if __name__=='__main__':
    print(Euler_41())

