from time import time
cubes = [i**3 for i in range(1,10**3)]
def e341(target = 153506976):
    t = time()
    ref={1:1,3:2,5:3,}
    keys = list(ref.keys())
    mini = 10000
    j = 5
    jx = 2
    b = True
    test = target/10**4
    for i in range(4,target+1):
        if i>mini:mini+=10000;print('i:',i,'tdiff:',i/target,len(keys)+1,\
                'time',(time()-t)*test);t = time()

        if j<i:
            jx += 1 
            j = keys[jx]
        k = ref.get(j)
        ref[k+keys[-1]]=i
        keys+=[k+keys[-1]]
        if ref.get(keys[-1])>=target:return keys[-1]
    x = [10**6<=i for i in keys]
    print(ref.get(keys[x.index(True)]))
    return ref
    
    
if __name__=='__main__':
    e341()
