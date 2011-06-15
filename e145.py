#!/usr/bin/python
import itertools, functools, operator
 
def s(n, f):
    return 19 - n if n >= 10 else max(n - 1, 0) if f else n + 1
def Euler_145():
    c = 0
    for k in range(1, 10):
        for n in itertools.product(
            *(k // 2 * [range(19)] + k % 2 * [range(10)])):
            if n[0]:
                x = sum(n[i] * (10 ** i + 10 ** (k - i - 1))
                        for i in range((k + 1) // 2))
                if set(str(x)) <= {'1', '3', '5', '7', '9'}:
                    a = functools.reduce(
                        operator.mul,
                        (s(n[i], i == 0) for i in range(k // 2)), 1)
                    c += a
    return c

if __name__=='__main__':
    print(Euler_145())
