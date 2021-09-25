def sortedSquaredArray(array):
    new_ar = [x ** 2 for x in array]
    l = len(new_ar)
    while True:
        i = 0
        while i < l - 1 and new_ar[i] > new_ar[i + 1]:
            new_ar[i], new_ar[i + 1] = new_ar[i + 1], new_ar[i]
            i += 1
        if i == 0:
            break
    return new_ar
