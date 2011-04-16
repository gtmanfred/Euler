def Euler_3(num=600851475143):
    primes = []
    i =2 
    while i <= num:
        if num%i ==0 and isprime(i):
            num = num//i
            primes = primes +[i] 
            i = 2
        i += 1
    return max(primes)
 
def isprime(n):
    i = 2
    while i<n:
        if n%i ==0:
            return False
        i += 1
    return True

if __name__=='__main__':
    print(Euler_3())
