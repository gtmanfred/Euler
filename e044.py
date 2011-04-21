maxpn = 2000
pn = list(int((n*(3*n-1))/2) for n in range(1, 2*maxpn+1))
pd = dict.fromkeys(pn,1)
def Euler_44():
    
    for i in range(maxpn):
        it = pn[i]
        for j in range(i+1,2*maxpn):
            jt = pn[j]
            if jt!=it:
                pdif = jt-it
                psum = jt+it
                if pd.get(pdif) and pd.get(psum):
                    return (jt-it)
                    '''
                    d = jt-it
                    if d<mind:
                        mind = d
                        print(mind)
                    '''
    #d = [(int(i)-int(j)) for i in pn.keys() for j in pn.keys() if j!=i and
           ### pn.get(j-i) and pn.get(j+i)]
    return maxd

if __name__=='__main__':
    print(Euler_44())

