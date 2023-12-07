from functools import cmp_to_key, partial

input_path = 'input/7_Camel_Cards.txt'


CARDS = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


COMBS = {
    '5kind': 7,
    '4kind': 6,
    'fullhouse': 5,
    '3kind': 4,
    '2pairs': 3,
    '1pair': 2,
    'high': 1,
}


def get_card_bids():
    card_bids = {}
    with open(input_path) as f:
        for line in f:
            parts = line.split()
            card_bids[parts[0]] = int(parts[1])
    return card_bids


def check_comb(hand, new=False):
    labels = {}
    for c in hand:
        if c not in labels:
            labels[c] = 0
        labels[c] += 1

    if new and 'J' in labels:
        if len(labels) != 1:
            js = labels.pop('J')
            k = max(labels, key=labels.get)
            labels[k] += js

    comb_type = 'high'
    len_h = len(labels)
    if len_h == 5:
        comb_type = 'high'
    if len_h == 4:
        comb_type = '1pair'
    if len_h == 3:
        for v in labels.values():
            if v == 3:
                comb_type = '3kind'
                break
        else:
            comb_type = '2pairs'
    if len_h == 2:
        for v in labels.values():
            if v == 4:
                comb_type = '4kind'
                break
        else:
            comb_type = 'fullhouse'
    if len_h == 1:
        comb_type = '5kind'

    return comb_type


def sort_hands(x, y, new=False):
    x_comb = check_comb(x, new)
    y_comb = check_comb(y, new)
    if COMBS[x_comb] == COMBS[y_comb]:
        for c1, c2 in zip(x, y):
            if CARDS[c1] == CARDS[c2]:
                continue
            return CARDS[c1] - CARDS[c2]
    return COMBS[x_comb] - COMBS[y_comb]


def solution1():
    card_bids = get_card_bids()
    hands = sorted(list(card_bids.keys()), key=cmp_to_key(sort_hands))
    score = []
    for i, h in enumerate(hands):
        score.append(card_bids[h] * (i + 1))
    return sum(score)


def solution2():
    CARDS['J'] = 1
    card_bids = get_card_bids()
    hands = sorted(list(card_bids.keys()), key=cmp_to_key(partial(sort_hands, new=True)))
    score = []
    for i, h in enumerate(hands):
        score.append(card_bids[h] * (i + 1))
    return sum(score)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
