'''
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
'''
def Euler_2_2(num = 2**40000):
    (a,b)=(1,2)
    tot = b
    while b<=num:
        (a,b) = (b,a+b)
        (a,b) = (b,a+b)
        (a,b) = (b,a+b)
        if b<=num:
            tot+=b
    return tot


if __name__ == '__main__':
    print(Euler_2_2())
