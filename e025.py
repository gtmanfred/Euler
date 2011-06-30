def e025(n=1000):
    new = '1'
    last = '1'
    i = 2
    while len(new)<n:
        i+=1
        last,new=new,str(eval(last+'+'+new))
    return i
def Euler_25(num = 1000):
    new = '1'
    last = '1'
    i = 2 
    while len(new)<num:
        i+=1
        hold = new
        new = str(int(new)+int(last))
        last = hold
    return i 

if __name__=='__main__':
    #print(e025())
    print(Euler_25())
