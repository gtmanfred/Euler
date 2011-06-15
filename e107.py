def e107():
    tmp = open('network.txt').read().split('\n')[:-1]
    alist = []
    tot = 0
    for line in tmp:
        alist.append(line.split(','))
    for line in alist:
        for i in line:
            if i=='-':continue
            tot += int(i)
    maxtot = tot//2
    return maxtot
if __name__=='__main__':
    print(e107())
