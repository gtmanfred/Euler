from math import log10
def Euler_63():
    s = 0
    maxi = 10
    for i in range(1,maxi):
        logi = log10(i)
        s+=int(1/(1-logi))
    return s

if __name__=='__main__':
    print(Euler_63())
    print(__name__)
