fact = [1,1,2,6,24,120,720,5040,40320,362880]

def sepdigs(num):return [int(x) for x in str(num)]

def Euler_74():
    count = 0
    for i in range(1,10**6):
        if i%10**4==0:print('i:',i//10**4)
        chain = 0
        num = i
        nset = set()
        while not num in nset:
            nset.add(num)
            num1 = [int(x) for x in str(num)]
            num = sum([fact[x] for x in num1])
        if len(nset)==60:count+=1;print('Count:',count)
    return count


if __name__=='__main__':
    print(Euler_74())
