from collections import Counter
from operator import itemgetter
 
def evaluate(cards):
    assert len(cards) == 5
    ranks = [evaluate.ranks_by_symbol[c[0]] for c in cards]
    ranks.sort(reverse=True)
    unique_ranks = list(Counter(ranks).items())
    unique_ranks.sort(key=itemgetter(0), reverse=True)
    unique_ranks.sort(key=itemgetter(1), reverse=True)
    n = len(unique_ranks)
    straight = (n == 5 and
        ranks[0] - ranks[-1] == n - 1 and
        all(r <= ranks[0] and r >= ranks[-1] for r in ranks))
    one_pair = n == 4
    two_pair = n == 3 and unique_ranks[0][1] == 2 
    three_of_kind = n == 3 and unique_ranks[0][1] == 3
    full_house = n == 2 and unique_ranks[0][1] == 3
    four_of_kind = n == 2 and unique_ranks[0][1] == 4
    flush = all(c[1] == cards[0][1] for c in cards)
    hand = 0
    if one_pair:
        hand = 10
    elif two_pair:
        hand = 20
    elif three_of_kind:
        hand = 30
    elif straight:
        hand = 40 if not flush else 80
    elif flush:
        hand = 50
    elif full_house:
        hand = 60
    elif four_of_kind:
        hand = 70
    if two_pair or full_house:
        hand_value = (unique_ranks[0][0], unique_ranks[1][0])
    else:
        hand_value = (unique_ranks[0][0],)
    return (hand, hand_value, tuple(ranks))
evaluate.ranks_by_symbol = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5,
    '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
 
wins = 0
with open('script/poker.txt') as f:
    f = f.read().split('\n')[1:-1]
    for line in f:
        tokens = line.split()
        hand1 = tokens[:5]
        hand2 = tokens[5:]
        if evaluate(hand1) > evaluate(hand2):
            wins += 1
print(wins)
