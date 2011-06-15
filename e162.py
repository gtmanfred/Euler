memo = dict()
def e162(left, start, Z=0, O=0, A=0):
    keys = memo.keys()
    if left<start and (left, Z, O, A) in keys: return memo[left, Z, O, A]
    elif left==0: s = 1 if Z and O and A else 0
    elif Z and O and A: s = (16**left)
    else:
        s  = e162(left-1, start, 1, O, A) if left<start else 0
        s += e162(left-1, start, Z, 1, A)
        s += e162(left-1, start, Z, O, 1)
        s += e162(left-1, start, Z, O, A) * 13
    if left<start: memo[left, Z, O, A] = s
    return s
if __name__=='__main__':
    print(hex(sum(e162(i,i) for i in range(17))).upper()[2:])
