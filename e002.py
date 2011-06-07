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
    print(Euler_2())
