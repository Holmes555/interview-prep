def minimumWaitingTime(queries):
    queries.sort()
    result = 0
    arr = []
    for q in queries[:-1]:
        result += q
        arr.append(result)
    return sum(arr)
