with open('script/poker.txt') as f:
    alist = list(x for x in f.read().split('\n'))[1:]
blist = []
count = 0
def Euler_54():
    for x in alist[:-1]:
        y = x.split(' ')
        blist.append([y[:5],y[5:]])
    return blist 
if __name__=='__main__':
    print(Euler_54())
