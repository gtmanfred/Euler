from time import time
def e001(top=1000):
    return sum([i for i in range(1,top) if i%5==0 or i%3==0])
def e1(top=1000):
    a = [1]*(top+1)
    for i in range(3,top+1,3):
        if a[i]:a[i]=0;
    for i in range(5,top+1,5):
        if a[i]:a[i]=0;
    return sum([i for i in range(1,top+1) if a[i]])
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
    t =time()
    print(e1())
    print(time()-t)
    t = time()
    print(e001())
    print(time()-t)
    #print(Euler_1(1000))
