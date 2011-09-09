def e103():
    n = 7
    A = [11,18,19,20,22,25]
    tmp = len(A)//2
    b = A[tmp]
    ret = [str(b)]
    for x in A:
        ret+=[str(b+x)]
    return ''.join(ret)
if __name__=='__main__':
    print(e103())
