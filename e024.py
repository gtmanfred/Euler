import itertools
def Euler_24(num=10**6):
    x = itertools.permutations('0123456789',10)
    count = 0
    for i in x:
        count+=1
        if count == num:
            return i


if __name__=='__main__':
    print(Euler_24())
