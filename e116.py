from script.math2 import bicoeff
def e116(m=50,an=[2,3,4]):
	return sum(f(m, n) for n in an)
def f(m, n):
    num_ways = 0
    for b in range(1, m // n + 1):
        num_ways += bicoeff(m - b * (n - 1), b)
    return num_ways
if __name__=='__main__':
    print(e116())
