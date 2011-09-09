from script.maths import sumdigs
def e119(top =30):
    alist = []
    b = 2
    while True:
        for e in range(2,50):
            tmp = b**e
            if sumdigs(tmp)==b:alist.append(tmp)
        if len(alist)==top+1:return alist[top]
        b+=1
            
if __name__=='__main__':
    print(e119(30))
