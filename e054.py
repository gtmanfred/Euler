alist = list(x for x in open('poker.txt').read().split('\n'))
blist = []
count = 0
for x in alist[:-1]:
    y = x.split(' ')
    blist.append([y[:5],y[5:]])
    print([y[:5],y[5:]])
    if input()==1:count+=1
print(count)
def Euler_54():
    pass

if __name__=='__main__':
    print(Euler_54())
