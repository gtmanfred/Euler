from script.newton import newton
def e235(k=5000,sk = -6*10**11):
    u = lambda k,r:(900-3*k)*r**(k-1)
    s = lambda r:sum([u(k,r) for k in range(1,5001)])
    print(newton(s))
e235()

