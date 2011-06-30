from math import sqrt
def atkins(limit=1000000):
    '''use sieve of atkins to find primes <= limit.'''
    primes = [0] * limit

    # n = 3x^2 + y^2 section
    xx3 = 3
    for dxx in range( 0, 12*int( sqrt( ( limit - 1 ) / 3 ) ), 24 ):
        xx3 += dxx
        y_limit = int(12*sqrt(limit - xx3) - 36)
        n = xx3 + 16
        for dn in range( -12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]

        n = xx3 + 4
        for dn in range( 12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]

    # n = 4x^2 + y^2 section
    xx4 = 0
    for dxx4 in range( 4, 8*int(sqrt((limit - 1 )/4)) + 4, 8 ):
        xx4 += dxx4
        n = xx4+1

        if xx4%3:
            for dn in range( 0, 4*int( sqrt( limit - xx4 ) ) - 3, 8 ):
                n += dn
                primes[n] = not primes[n]

        else:
            y_limit = 12 * int( sqrt( limit - xx4 ) ) - 36

            n = xx4 + 25
            for dn in range( -24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]

            n = xx4+1
            for dn in range( 24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]

    # n = 3x^2 - y^2 section
    xx = 1
    for x in range( 3, int( sqrt( limit / 2 ) ) + 1, 2 ):
        xx += 4*x - 4
        n = 3*xx

        if n > limit:
            min_y = ((int(sqrt(n - limit))>>2)<<2)
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4

        else:
            s = 4

        for dn in range( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    xx = 0
    for x in range( 2, int( sqrt( limit / 2 ) ) + 1, 2 ):
        xx += 4*x - 4
        n = 3*xx

        if n > limit:
            min_y = ((int(sqrt(n - limit))>>2)<<2)-1
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4

        else:
            n -= 1
            s = 0

        for dn in range( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    # eliminate squares
    for n in range(5,int(sqrt(limit))+1,2):
        if primes[n]:
            for k in range(n*n, limit, n*n):
                primes[k] = False

    return [2,3] + list(filter(primes.__getitem__, range(5,limit,2)))
