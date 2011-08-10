def u(n):
    return sum((-1 if k & 1 else 1) * n ** k for k in range(11))
def e101(): 
    sequence = [u(n) for n in range(1, 11)]
    fit_sum = 0
    for k in range(1, 11):
        diffs = [sequence[:k]] + [None] * (k - 1)
        for i in range(k - 1):
            d_i = diffs[i]
            d_i_1 = [0] * (k - 1 - i)
            for j in range(k - 1 - i):
                d_i_1[j] = d_i[j + 1] - d_i[j]
            diffs[i + 1] = d_i_1
        diffs[-1].append(diffs[-1][-1])
        for i in range(1, k):
            diffs[k - 1 - i].append(diffs[k - 1 - i][-1] + diffs[k - i][-1])
        fit_sum += diffs[0][-1]
    return fit_sum
if __name__=='__main__':
    print(e101())
