from itertools import combinations

def issumset(a):
    return rule2(a) and rule1(a)

def rule1(a):
    n = len(a)
    sums = set()
    for i in range(1, n):
        for j in combinations(a, i):
            sssum = sum(j)
            if sssum in sums:
                return False
            else:
                sums.add(sssum)
    return True

def rule2(a):
    n = len(a)
    for i in range(1, (n + 1) // 2):
        if sum(a[:i + 1]) <= sum(a[-i:]):
            return False
    return True
