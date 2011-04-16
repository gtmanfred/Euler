'''def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b // gcd(a,b)

def Euler_5(num = 20):
    n = 1
    for i in range(1,num+1):
        n = lcm(n, i)
    return n
'''
import isprime
def Euler_5(top=20):
    val =1
    for i in range(1,top+1):
        if isprime.isprime(i):
            num = i
            while num<=top:
                num = num*i
        val *=(num//i)
    return val
    
if __name__=='__main__':
    print(Euler_5())
