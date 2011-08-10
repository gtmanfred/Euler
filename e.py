def f(k):
	if k % 6 == 0:
		return 3 * (k // 6)
	if k % 6 == 1:
		return 4 * (k // 6) + 1
	if k % 6 == 2:
		return 3 * (k // 6) + 1
	if k % 6 == 3:
		return k // 6
	if k % 6 == 4:
		return (k // 6) * 6 + 3
	if k % 6 == 5:
		return k // 6
 
n = 10 ** 12
m = 10 ** 6
c = [0] * (m * 6 + 1)
d = [0] * m
 
for i in range(1, m * 6 + 1):
    c[i] += (c[i - 1] + f(i)) % m
    d[c[i]] += (n - i) // (m * 6) + 1
 
print(sum(x * (x - 1) // 2 for x in d) + d[c[-1]])