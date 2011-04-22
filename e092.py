def digs(num):
    res = 0 
    while num > 9:
        res,num = res+(num%10)**2,num//10
    return res+(num**2)

def Euler_92():
    alist = [i for i in range(1,570)]
    nums = dict.fromkeys(alist,0)
    for i in nums.keys():
        num = int(i)
        while num != 89 and num != 1:
            num = digs(num)
        if num==89:nums[i]=1
    count = 0
    for j in range(1,10000000):
        k = digs(j)
        if nums.get(k):count+=1
        if j%100000==0:print(j//100000)
    return count

if __name__=='__main__':
    print(Euler_92())
