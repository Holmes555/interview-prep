input_path = 'input/10_Pipe_Maze.txt'


def get_maze():
    maze = []
    with open(input_path) as f:
        for line in f:
            maze.append(list(line))
    return maze


def make_move(i, j, maze, weights, pool, value='-'):

    def add_coords(n, m):
        if (n, m) not in weights:
            pool.append(((n, m), weights[(i, j)] + 1))

    val = maze[i][j]
    if val == 'S':
        val = value
    if val == '|':
        add_coords(i + 1, j)
        add_coords(i - 1, j)
    if val == '-':
        add_coords(i, j + 1)
        add_coords(i, j - 1)
    if val == 'L':
        add_coords(i - 1, j)
        add_coords(i, j + 1)
    if val == 'J':
        add_coords(i - 1, j)
        add_coords(i, j - 1)
    if val == '7':
        add_coords(i + 1, j)
        add_coords(i, j - 1)
    if val == 'F':
        add_coords(i + 1, j)
        add_coords(i, j + 1)


def solution1():
    maze = get_maze()
    start = (25, 32)
    weights = {}
    pool = [(start, 0)]
    max_w = 0
    while pool:
        move = pool.pop(0)
        weights[move[0]] = move[1]
        make_move(*move[0], maze, weights, pool)
        if move[1] > max_w:
            max_w = move[1]
    return max_w


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
    # print(solution2())
