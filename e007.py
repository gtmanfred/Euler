from maths import isprime
def Euler_7(n = 10001):
    i =1 
    num = 0;
    while i<n:
        num +=1
        if isprime(num):
            i +=1
    return num 

def isprime(n):
        i =2 
        if (n%2 is 0) or (n%3 is 0):
            return False
        while i*i<=n:
            if n%i ==0:
                return False
            i += 1
        return True

if __name__=='__main__':
    print(Euler_7())
