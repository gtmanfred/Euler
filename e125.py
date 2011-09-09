from script.maths import *
from math import sqrt
def Euler_125(top = 10**8):
    count = 0
    nums = set()
    t = top
    top = int(top**.5)
    for i in range(1,top):
        num = i*i
        for j in range(i+1,top):
            num+=j**2
            if num>=t:break
            if ispal(num):
                nums.add(num)
                count+=1
    return [sum(nums),count]
                
if __name__=='__main__':
    print(Euler_125())
