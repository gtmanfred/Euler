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
