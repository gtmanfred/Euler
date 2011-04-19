from maths import ispan
def Euler_38():
    n = 9
    i = 1
    high = 0
    while len(str(i))<=9//2:
        x = 2
        t = i
        string = str(i)
        while len(string)<=9:
            t*=x
            string += str(t)
            if len(string)==9 and ispan(int(string)):
                if int(string)>high:
                    high = int(string)
                    
        i+=1
    return high

if __name__=='__main__':
    print(Euler_38())
