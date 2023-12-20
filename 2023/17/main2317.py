def get_new_candidates(lines, vertex, val, height, width, min_m, max_m):
    candidates = []
    s0p = int(lines[vertex[1]][vertex[2]])
    s0n = int(lines[vertex[1]][vertex[2]])
    if vertex[0] == 0:
        for i in range(1, min_m):
            if vertex[1] + i < height:
                s0p += int(lines[vertex[1] + i][vertex[2]])
            if vertex[1] - i >= 0:
                s0n += int(lines[vertex[1] - i][vertex[2]])
        for i in range(min_m, max_m):
            if vertex[1] + i < height:
                candidates.append((1, vertex[1] + i, vertex[2], val + s0p))
                s0p += int(lines[vertex[1] + i][vertex[2]])
            if vertex[1] - i >= 0:
                candidates.append((1, vertex[1] - i, vertex[2], val + s0n))
                s0n += int(lines[vertex[1] - i][vertex[2]])
    elif vertex[0] == 1:
        for i in range(1, min_m):
            if vertex[2] + i < width:
                s0p += int(lines[vertex[1]][vertex[2] + i])
            if vertex[2] - i >= 0:
                s0n += int(lines[vertex[1]][vertex[2] - i])
        for i in range(min_m, max_m):
            if vertex[2] + i < width:
                candidates.append((0, vertex[1], vertex[2] + i, val + s0p))
                s0p += int(lines[vertex[1]][vertex[2] + i])
            if vertex[2] - i >= 0:
                candidates.append((0, vertex[1], vertex[2] - i, val + s0n))
                s0n += int(lines[vertex[1]][vertex[2] - i])
    return candidates


def main(min_m, max_m):
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        width = len(lines[0])
        height = len(lines)

        # 0: horizontal, 1: vertical movement | row ind | col ind
        reached: dict[tuple[int, int, int], int] = {}
        candidates: dict[tuple[int, int, int], int] = {}
        reached[(0, height - 1, width - 1)] = 0
        reached[(1, height - 1, width - 1)] = 0
        raw_candidates = get_new_candidates(lines, (0, height - 1, width - 1), 0, height, width, min_m, max_m) +\
            get_new_candidates(lines, (1, height - 1, width - 1), 0, height, width, min_m, max_m)
        for raw_candidate in raw_candidates:
            candidates[(raw_candidate[0], raw_candidate[1], raw_candidate[2])] = raw_candidate[3]

        while len(candidates) > 0 and ((0, 0, 0) not in reached or (1, 0, 0) not in reached):
            minn = 10 ** 10
            key = None
            for cand, value in candidates.items():
                if value < minn:
                    minn = value
                    key = (cand[0], cand[1], cand[2])
            assert key not in reached
            reached[key] = minn
            del candidates[key]
            new_candidates = get_new_candidates(lines, key, reached[key], height, width, min_m, max_m)

            for candidate in new_candidates:
                key = (candidate[0], candidate[1], candidate[2])
                if key in reached:
                    assert reached[key] < candidate[3]
                elif key in candidates:
                    if candidates[key] > candidate[3]:
                        candidates[key] = candidate[3]
                else:
                    candidates[key] = candidate[3]

        print(min(reached[(0, 0, 0)], reached[(1, 0, 0)]))


if __name__ == "__main__":
    main(1, 4)
    main(4, 11)
