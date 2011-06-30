from math2 import binomial_coefficient, multinomial_coefficient
def e117():
    units = 50
    num_ways = 0
    for r in range(units // 2 + 1):
        for g in range((units - 2 * r) // 3 + 1):
            for b in range((units - 2 * r - 3 * g) // 4 + 1):
                p = units - 2 * r - 3 * g - 4 * b + r + g + b
                blocks = r + g + b
                c1 = binomial_coefficient(p, blocks)
                c2 = multinomial_coefficient(blocks, (r, g, b))
                num_ways += c1 * c2
    return num_ways
if __name__=='__main__':
    print(e117())
