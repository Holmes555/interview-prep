input_path = 'input/5_If_You_Give_A_Seed_A_Fertilizer.txt'


def get_seeds_and_maps(new=False):
    seeds = []
    seeds_maps = []
    i = -1
    with open(input_path) as f:
        for line in f:
            if 'seeds:' in line:
                parts = line.split(': ')
                s = parts[1].split()
                if new:
                    for j in range(0, len(s), 2):
                        seeds.extend([(int(s[j]), int(s[j + 1]))])
                else:
                    seeds = map(int, s)
            elif 'map:' in line:
                i += 1
                seeds_maps.append({})
            else:
                numbers = line.split()
                if len(numbers) == 3:
                    seeds_maps[i].update({int(numbers[1]): (int(numbers[0]), int(numbers[2]))})
    return seeds, seeds_maps


def get_soonest_seed(seeds, seeds_maps):
    for smap in seeds_maps:
        cur_seeds = []
        sorted_k = sorted(smap)
        for s in seeds:
            for i, v in enumerate(sorted_k):
                if s < v:
                    if i == 0:
                        res = s
                        break
                    key = sorted_k[i - 1]
                    diff = s - key
                    if diff <= smap[key][1]:
                        res = smap[key][0] + diff
                    else:
                        res = s
                    break
            else:
                key = sorted_k[i]
                diff = s - key
                if diff <= smap[key][1]:
                    res = smap[key][0] + diff
                else:
                    res = s
            cur_seeds.append(res)
        seeds = cur_seeds.copy()
    return min(seeds)


def get_soonest_range_seed(seeds, seeds_maps):
    for smap in seeds_maps:
        cur_seeds = []
        sorted_k = sorted(smap)
        ind = 0
        while ind < len(seeds):
            cur_s = seeds[ind]
            s = cur_s[0]
            for i, v in enumerate(sorted_k):
                if s < v:
                    if i == 0:
                        res = s
                        next_diff = sorted_k[i] - s
                    else:
                        key = sorted_k[i - 1]
                        diff = s - key
                        if diff <= smap[key][1]:
                            res = smap[key][0] + diff
                        else:
                            res = s
                        next_diff = key + smap[key][1] - s
                    cur_diff = cur_s[1] - next_diff
                    if cur_diff > 0:
                        if next_diff == 0:
                            cur_seeds.append((s, v - s))
                            seeds.append((v, s + cur_s[1] - v))
                            break
                        seeds.append((s + next_diff, cur_diff))
                        old_diff = next_diff
                    else:
                        old_diff = cur_s[1]
                    final_res = (res, old_diff)
                    break
            else:
                key = sorted_k[i]
                diff = s - key
                if diff <= smap[key][1]:
                    res = smap[key][0] + diff
                    next_diff = key + smap[key][1] - s
                    cur_diff = cur_s[1] - next_diff
                    if cur_diff > 0:
                        cur_seeds.append((s + next_diff, cur_diff))
                        old_diff = next_diff
                    else:
                        old_diff = cur_s[1]
                else:
                    res = s
                    old_diff = cur_s[1]
                final_res = (res, old_diff)
            cur_seeds.append(final_res)
            ind += 1
        seeds = cur_seeds.copy()
    return min(seeds)[0]


def solution1():
    seeds, seeds_maps = get_seeds_and_maps()
    return get_soonest_seed(seeds, seeds_maps)


def solution2():
    seeds, seeds_maps = get_seeds_and_maps(True)
    return get_soonest_range_seed(seeds, seeds_maps)


if __name__ == '__main__':
    print(solution1())
    print(solution2())
