def Euler_48(num=1000):
    ans=sum([elem**elem for elem in range(1,num+1)])%10**10
    return ans

if __name__=='__main__':
    print(Euler_48())
