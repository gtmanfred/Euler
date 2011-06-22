class Totient:
    def __init__(self, n):
        self.totients = [1 for i in range(n)]
        for i in range(2, n):
            if self.totients[i] == 1:
                for j in range(i, n, i):
                    self.totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]
