def e122(limit=200):
    costs_and_powers = {1: (0, [{1}])}
    for n in range(2, limit + 1):
        min_cost = float('inf')
        intermediary_powers = []
        for m in range((n + 1) // 2, n):
            cost, powers = costs_and_powers[m]
            if cost > min_cost:
                continue
            else:
                new_powers = [p | {n} for p in powers if n - m in p]
                if new_powers:
                    if cost < min_cost:
                        del intermediary_powers[:]
                        min_cost = cost
                    intermediary_powers.extend(new_powers)
        costs_and_powers[n] = (min_cost + 1, intermediary_powers)
    print(costs_and_powers[15])
    return sum(costs_and_powers[n][0] for n in range(1, limit + 1))
if __name__=='__main__':
    print(e122())
