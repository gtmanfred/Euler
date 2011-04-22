def Euler_57():
    num = 3
    den = 2
    i = 1
    count = 0
    while i<=1000:
        hold = num
        num = num+den+den
        den = hold+den
        if len(str(num))>len(str(den)):count+=1
        i+=1
    return count

if __name__=='__main__':
    print(Euler_57())
