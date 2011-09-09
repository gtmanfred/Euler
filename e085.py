from math import sqrt
def count(x,y):
    count = 0 
    for i in range(0,x):
        for j in range(0,y):
            count += (x-i)*(y-j)
    return count

def Euler_85(top=2000000):
    mindiff =top 
    for i in range(1,100):
        print(i)
        for j in range(1,i):
            diff = abs(top-count(i,j))
            if diff<mindiff:mindiff=diff;reti = i;retj=j;ret = i*j#
    print(count(i,j))
    print('i:',reti,'j:',retj)
    return ret

if __name__=='__main__':
    print(Euler_85())
