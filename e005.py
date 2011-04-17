import maths
def Euler_5(top=20):
    val =1
    for i in range(1,top+1):
        if maths.isprime(i):
            num = i
            while num<=top:
                num = num*i
            val *=(num//i)
    return val
    
if __name__=='__main__':
    print(Euler_5())
