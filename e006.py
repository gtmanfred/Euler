def Euler_6(num=100):
    square = sum([elem**2 for elem in range(num+1)])
    sums = sum([elem for elem in range(num+1)])**2
    return sums-square

if __name__=='__main__':
    print(Euler_6())
