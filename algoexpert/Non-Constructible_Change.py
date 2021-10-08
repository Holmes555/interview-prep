def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for c in coins:
        if c <= change + 1:
            change += c
        else:
            break
    return change + 1
