def Euler_1(num = 1000):
    #aset = set()
    a =[]
    for i in range(num):
        if i%5 ==0 or i%3 ==0:
            a=a+[i]
            #   aset.add(i)
           #    aset.add(i)
   # print(aset)
   # ans = 0
   # while (len(aset)>0):
    #    print(a = sum(aset))
       # ans += aset.pop()
    return sum(a)

if __name__ == '__main__':
    print(Euler_1(1000))
