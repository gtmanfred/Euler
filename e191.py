f_db={};
def e191(left,nl,na):
    if(nl>=3): return 0;
    if(na>1): return 0;
    if(left<=0): return 1;
 
    key="%d %d %d"%(left,nl,na);
    if(key in f_db): return f_db[key];
 
    total=0;
    total+=e191(left-1,0,na);
    total+=e191(left-1,nl+1,na);
    total+=e191(left-1,0,na+1);
 
    f_db[key]=total;
    return total;
 
print(e191(30,0,0))
