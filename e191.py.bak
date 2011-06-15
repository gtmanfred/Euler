times = ['O','L','A']
top = 0
def e191(n=4):
    global top 
    top = n
    s = pattern(n)
    return s
def pattern(n):
    print(n)
    if n==1:
        return ['0','L','A']
    elif n<3:
        p = pattern(n-1)
        p = [i+j for i in p for j in times if test(i,j)]
        if n==2:
            p = {i:[p[i-1]] for i in range(1,9)}
        return (p)
    else:
        if n == 3:
            p = pattern(n-1)
            p1 = p.get(1)
            p2 = p.get(2)
            p3 = p.get(3)
            p4 = p.get(4)
            p5 = p.get(5)
            p6 = p.get(6)
            p7 = p.get(7)
            p8 = p.get(8)
        else:
            p1,p2,p3,p4,p5,p6,p7,p8 = pattern(n-1)
#        print(p1,p2,p3,p4,p5,p6,p7,p8)
        p1 = [i+j for j in times for i in p1 if test(i,j)]
        p2 = [i+j for j in times for i in p2 if test(i,j)]
        p3 = [i+j for j in times for i in p3 if test(i,j)]
        p4 = [i+j for j in times for i in p4 if test(i,j)]
        p5 = [i+j for j in times for i in p5 if test(i,j)]
        p6 = [i+j for j in times for i in p6 if test(i,j)]
        p7 = [i+j for j in times for i in p7 if test(i,j)]
        p8 = [i+j for j in times for i in p8 if test(i,j)]
        print(n)
        if n == top:
            return(len(p1)+len(p2)+len(p3)+len(p4)+len(p5)+len(p6)+len(p7)+len(p8))
        return p1,p2,p3,p4,p5,p6,p7,p8


def test(i,j):
    if j == 'L':
        if 'L' in i:return False
        else:return True
    elif j == 'A':
        if len(i)<2:return True
        elif i[-2]=='A' and i[-1]=='A':return False
        else:return True
    else:return True
if __name__=='__main__':
    print(e191(30))
