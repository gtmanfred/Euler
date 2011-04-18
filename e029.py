def Euler_25(a1=2,a2=100,b1=2,b2=100):
    nums = set()
    for i in range(a1,a2+1):
        for j in range(b1,b2+1):
            nums.add(i**j)
    
    count=0
    while nums:
        nums.pop()
        count+=1
    
    return count 

if __name__=='__main__':
    print(Euler_25())
