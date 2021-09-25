def isValidSubsequence(array, sequence):
    i = 0
    l = len(sequence)
    for c in array:
        if c == sequence[i]:
            i += 1
            if i == l:
                return True
    return False
