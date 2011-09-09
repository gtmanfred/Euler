from script.memorize import memo
a,b,c=21**7,7**21,12**7
def e340():
    quot,remain=divmod(b,a)
    s = quot * a * (2*f(b) + 3*(a-c)*(quot-1) - (a-1)) // 2
    s1 = (f(0) + f(remain)) * (remain+1) // 2
    return s+s1
def f(n):
    quot,remain=divmod(b-n,a)
    return b+(a-c)*(4+3*quot)-remain

if __name__=='__main__':
    print(e340()%10**9)
