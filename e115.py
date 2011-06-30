from e114 import f
def e115(m = 50,top = 10**6):
    n = m
    while f(m,n)<10**6:n+=1
    return n
if __name__=='__main__':
    print(e115())
