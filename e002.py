def e002(top=4*10**6):
    fib = [1,1]
    res = 0
    while fib[-1]<top:
        fib+=[fib[-1]+fib[-2]]
        if not fib[-1]&1:res+=fib[-1]
    return res

def Euler_2(num = 4000000):
    ans = 0
    last = 1
    i = 1
    while i <= num:
        if i%2 ==0:
            ans += i
        j = i
        i +=last
        last = j
    return ans


if __name__ == '__main__':
    print(e002())
    #print(Euler_2())
