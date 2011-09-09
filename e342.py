from script.helpers import *
def e342(n):
    count = 0
    mini = 1000
    for i in range(2,n):
        if i>mini:print(i/n);mini+=1000
        if test(i):
            count+=i
    return count
def test(i):
    phi = totient(i**2)
    tmp = primetree(phi)
    return all([tmp[i][1]==3 for i in range(len(tmp))])

if __name__=='__main__':
    print(e342(10**10))
