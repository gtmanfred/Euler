def primes(n):
    alist=[1 for i in range(n+1)]
    alist[0]=0
    alist[1]=0
    ret =[]
    t = 0
    for i in range(2,len(alist)):
        if alist[i]==1:
            if i>n//2 and t ==0:
                print(i)
                t =1
            for x in range(i**2,len(alist),i):
                alist[x]=0
    for j in range(n+1):
        if alist[j]==1:
            ret = ret+[j]
    return ret
    
def isprime(n):
    i =2 
    if (n==1):
        return False
    if (n==2)or(n==3):
        return True
    
    if (n%2 is 0) or (n%3 is 0):
        return False
    while i*i<=n:
        if n%i ==0:
            return False
        i +=1
    return True


def tree(num):
    ret = []
    i= 2
    while (isprime.isprime(num) is False):
        if (num%i==0):
            ret = ret+[i]
            num=num//i
            i =1
        i +=1
    ret = ret + [num]
    return ret

def ispal(num):
    num = str(num)
    while len(num)>1:
        if num[0] is not num[len(num)-1]:
            return False
        num = num[1:len(num)-1]
    return True



if __name__=='__main__':
    print(primes(10))
    print(isprime(17))
