def Euler_4(d=3):
    n = 10**d
    n2 =n//10 
    n = n-1
    ans = 0 
    for i in range(n2,n):
        for j in range(n2,n):
            if ispal(i*j):
                if ans<i*j:
                    ans = i*j
    return ans

def ispal(num):
    num = str(num)
    while len(num)>1:
        if num[0] is not num[len(num)-1]:
            return False
        num = num[1:len(num)-1]
    return True


if __name__=='__main__':
    print(Euler_4())
