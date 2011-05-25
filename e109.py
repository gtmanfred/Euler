def e109(n=100):
    count = 0
    scores = {}
    kdict = {}
    for i in range(1,21):
        scores['D'+str(i)]=2*i
        scores['T'+str(i)]=3*i
        scores['S'+str(i)]=i
    scores['D25']=50
    scores['S25']=25
    for i in scores.keys():
        if scores.get(i)<n and i[0]=='D':count+=1
        for j in scores.keys():
            if scores.get(i)+scores.get(j)<n and j[0]=='D':count+=1
            for k in scores.keys():
                tmp = scores.get(i)+scores.get(j)+scores.get(k)
                if (tmp<n and k[0]=='D'):
                    if kdict.get(k):
                        if (sorted([i,j]) in kdict.get(k)):break
                    if kdict.get(k):
                        kdict[k].append(sorted([i,j]))
                    else:kdict[k]=[sorted([i,j])]
                    count+=1;
    return count


if __name__=='__main__':
    print(e109())
