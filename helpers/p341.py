from time import time
def Euler_341(start = 1,limit=10**6):
    ''' Returns the sum of all the elements of the Golomb sequence
    	1 <= n < limit**3
    '''
    try:
        clist = [0, 1, 2]
        total = 0
        i = 0
        j = 2
        jcount = 1
        s = 0
        base = 1
        base3 = base ** 3
        n = limit ** 3
        while base < limit:
            i += 1
            total += clist[i]
            while base3 <= min(n-1,total):
                s += i
                base += 1
                base3 = base ** 3
            # Add to list if necessary  
            if i == len(clist)-1:
                clist.append(j)
                jcount += 1
                if jcount == clist[j]:
                    j += 1
                    jcount = 0
        return s
    except:return [base,base3,len(clist),i]
if __name__ == '__main__':
    t = time()
    print(Euler_341())
    print(time()-t)

