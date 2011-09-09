from script import maths
from script import names
from script.maths import letters
def e022(t = 'script/names.txt'):
    with open(t) as file:
        f = file.read().split('\n')[1]
        f = f.split('","')
        f[0],f[-1]=f[0][1:],f[-1][:-1]
        f = sorted(f)
        sums = 0
        for i,j in enumerate(f):
            score = sum([int(letters.get(x)) for x in j])
            sums +=score*(i+1)
        return sums
def Euler_22():
    name = sorted(names.names)
    ret = 0
    
    for i in range(len(name)):
        n = 0
        for j in range(len(name[i])):
           n += int(maths.letters[name[i][j]])
        ret+=n*(i+1)
    return ret

if __name__=='__main__':
    print(e022())
    #print(Euler_22())
