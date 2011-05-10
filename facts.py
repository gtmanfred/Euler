def factors(n):
    fact=[1,n]
    check=2
    rootn=n**.5
    while check<rootn:
        if n%check==0:
            fact.append(check)
            fact.append(n/check)
        check+=1
    if rootn==check:
        fact.append(check)
        fact = sorted(fact)
    return fact
def numfacts(n):
    fact=2
    check=2
    rootn=n**.5
    while check<rootn:
        if n%check==0:
            fact+=2
        check+=1
    if rootn==check:
        fact +=1
    return fact
