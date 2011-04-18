import maths
import names
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
    print(Euler_22())
