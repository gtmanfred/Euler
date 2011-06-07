def Euler_76(targ=100):
    nums = range(1,targ)
    way = [1]+[0]*targ
    for i in nums:
        for j in range(i,targ+1):
            way[j] += way[j-i]
    return way[targ]

if __name__=='__main__':
    print(Euler_76())
