def Euler_9(num=1000):
    for a in range(1,num):
        for b in range(1,num):
            if (a**2+b**2==(num-a-b)**2):
                ans = a*b*(num-a-b)
                return ans

if __name__=='__main__':
    print(Euler_9())
