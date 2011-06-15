signs = '+-*/'
from itertools import permutations
def e93():
    maxcount = 0
    maxnum = 0
    for i in range(1,7):
        print(i)
        for j in range(i+1,10):
            for k in range(j+1,10):
                for l in range(k+1,10):
                    num = ''.join([str(i),str(j),str(k),str(l)])
                    aset = test(num)
                    aset = {i for i in aset if i>0 and i%1==0}
                    if num == '1234':print(aset,len(aset))
                    if num == '1258':print(aset,len(aset))
                    count = 0
                    last = 0
                    b = False
                    while aset:
                        if 1 in aset or b:b=True
                        else:break
                        x = int(min(aset))
                        if last+1==x:
                            last = x
                            count+=1
                            aset.discard(x)
                        else:break
                    else:count = 0
                    if count>maxcount:
                        print(count,num)
                        maxcount = count
                        maxnum = num
    return maxnum
def test(vals):
    aset = set()
    perms = permutations(vals)
    perms = [''.join(i) for i in perms]
    for i in perms:
        aset.update(testsigns(i))
    return aset

def testsigns(vals):
    aset = set()
    for i in signs:
        for j in signs:
            for k in signs:
                try:aset.add(eval('(('+vals[0]+i+vals[1]+')'+j+vals[2]+')'+k+vals[3]))
                except:pass
                try:aset.add(eval('('+vals[0]+i+vals[1]+')'+j+'('+vals[2]+k+vals[3]+')'))
                except:pass
                try:aset.add(eval('('+vals[0]+i+'('+vals[1]+j+vals[2]+'))'+k+vals[3]))
                except:pass
                try:aset.add(eval(vals[0]+i+'('+vals[1]+j+'('+vals[2]+k+vals[3]+'))'))
                except:pass
                try:aset.add(eval(vals[0]+i+'(('+vals[1]+j+vals[2]+')'+k+vals[3]+')'))
                except:pass
#                try:aset.add(eval(vals[0]+i+'('+vals[1]+j+vals[2]+')'+k+vals[3]))
 #               except:pass
  #              try:aset.add(eval(vals[0]+i+vals[1]+j+vals[2]+k+vals[3]))
   #             except:pass
    return aset
if __name__=='__main__':
    print(e93())
