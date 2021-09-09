def twoNumberSum(array, targetSum):
    for i, first in enumerate(array):
        second = targetSum - first
        try:
            j = array.index(second)
        except ValueError:
            continue
        if i == j:
            continue
        return [array[i], array[j]]
    return []
