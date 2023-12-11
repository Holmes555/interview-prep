input_path = 'input/9_Mirage_Maintenance.txt'


def get_sequences():
    sequences = []
    with open(input_path) as f:
        for line in f:
            sequences.append(line.split())
    return sequences


def solution1():
    sequences = get_sequences()
    res = []
    for seq in sequences:
        new_seq = seq.copy()
        result = 0
        end = False
        while not end:
            end = True
            cur_seq = new_seq.copy()
            new_seq = []
            result += int(cur_seq[-1])
            for i in range(len(cur_seq) - 1):
                val = int(cur_seq[i + 1]) - int(cur_seq[i])
                if val != 0:
                    end = False
                new_seq.append(val)
        res.append(result)
    return sum(res)


def solution2():
    sequences = get_sequences()
    res = []
    for seq in sequences:
        new_seq = seq.copy()
        result = 0
        end = False
        j = 1
        while not end:
            end = True
            cur_seq = new_seq.copy()
            new_seq = []
            result += int(cur_seq[0]) * j
            for i in range(len(cur_seq) - 1):
                val = int(cur_seq[i + 1]) - int(cur_seq[i])
                if val != 0:
                    end = False
                new_seq.append(val)
            j *= -1
        res.append(result)
    return sum(res)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
