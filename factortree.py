import isprime

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
