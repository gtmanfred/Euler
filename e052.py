def Euler_52(Max=10**6,mult = 6):
    for i in range(10,Max+1):
        stri = str(i)
        listi = list(stri)
        data = {x:listi.count(x) for x in stri}
        if iseq(i,data,mult):return i

        
        
        
def iseq(i,data,num):
    for t in range(2,num+1):
        testd = {x:list(str(i*t)).count(x) for x in str(i)}
        if testd != data:return False
    return True
        
        
        
        
'''
        i2=i*2
        i3=i*3
        i4=i*4
        i5=i*5
        i6=i*6
        i2d = {x:list(str(i2)).count(x) for x in str(i2)}
        i3d = {x:list(str(i3)).count(x) for x in str(i3)}
        i4d = {x:list(str(i4)).count(x) for x in str(i4)}
        i5d = {x:list(str(i5)).count(x) for x in str(i5)}
        i6d = {x:list(str(i6)).count(x) for x in str(i6)}
'''

if __name__=='__main__':
    print(Euler_52())
