input_path = 'input/8_Treetop_Tree_House.txt'


def get_forest():
    forest = []
    with open(input_path) as f:
        for line in f:
            line = line.replace('\n', '')
            forest.append([int(v) for v in line])
    return forest


def is_visible(row, v):
    for tree in row:
        if v <= tree:
            return False
    return True


def calc_score(row, v):
    result = 0
    for tree in row:
        if v == tree:
            return result + 1
        if v > tree:
            result += 1
        if v < tree:
            return result
    return result


def solution1(forest):
    len_forest = len(forest)
    result = len_forest * 4 - 4
    for i in range(1, len_forest - 1):
        for j in range(1, len_forest - 1):
            v = forest[i][j]
            if (
                is_visible(forest[i][:j], v)
                or is_visible(forest[i][j + 1 : len_forest], v)
                or is_visible([column[j] for column in forest[:i]], v)
                or is_visible([column[j] for column in forest[i + 1 : len_forest]], v)
            ):
                result += 1
    return result


def solution2(forest):
    len_forest = len(forest)
    max_score = 0
    for i in range(1, len_forest - 1):
        for j in range(1, len_forest - 1):
            v = forest[i][j]
            score = (
                calc_score(reversed(forest[i][:j]), v)
                * calc_score(forest[i][j + 1 : len_forest], v)
                * calc_score(reversed([column[j] for column in forest[:i]]), v)
                * calc_score([column[j] for column in forest[i + 1 : len_forest]], v)
            )
            if score > max_score:
                max_score = score
    return max_score


if __name__ == '__main__':
    forest = get_forest()
    print(solution1(forest))
    print(solution2(forest))
