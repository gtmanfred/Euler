import maths
import words

tnums = list((i*(i+1))//2 for i in range(1,1001))
len(tnums)
alist = [1 for x in range(tnums[-1]+1)]
tndict = dict.fromkeys(alist,0)
tndict = dict.fromkeys(tnums,1)
def Euler_42():
    ret = 0
    for x in words.words:
        if tndict.get(sum(int(maths.letters.get(y)) for y in x)):
            ret += 1
    return ret
           

if __name__=='__main__':
    print(Euler_42())
