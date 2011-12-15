def e359():

def P(f,r):
    [firstfloor,vert,vert2]=findfirstfloor(r)
    if r%2:
        odd=2
    else:
        odd=-2
    val=firstfloor+vert;
    tween=odd;
    for i in range(2,f):
        if i%2:
            val+=vert2
            if r%2:
                vert2+=2;
            else:
                vert2+=6;
        else:
            val+=tween;
            tween+=odd;
    return val;

def findfirstfloor(r):
    tmp=1;
    iternum=2;
    vert1=1;
    vert2=4;
    while (iternum<=r):
        tmp+=iternum;
        if iternum%2:
            vert1-=1;
            vert2-=4;
        else:
            vert1+=3;
            vert2+=8;
        iternum+=1
    return [tmp,vert1,vert2]

if __name__=='__main__':
    print(P(10,20))
