neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def get_score(lines: list[list[int]], i, j) -> tuple[int, int]:
    height = len(lines)
    width = len(lines[0])

    reached: dict[int, dict[tuple, int]] = {0: {(i, j): 1}}
    for k in range(1, 10):
        reached[k] = {}
        for pos, rate in reached[k - 1].items():
            x, y = pos
            for nxa, nya in neighbours:
                cand = (x + nxa, y + nya)
                if 0 <= cand[0] < height and 0 <= cand[1] < width:
                    if lines[cand[0]][cand[1]] == k:
                        if cand not in reached[k]:
                            reached[k][cand] = rate
                        else:
                            reached[k][cand] += rate
    return len(reached[9]), sum(reached[9].values())


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        lines_n = []
        for line in lines:
            lines_n.append([])
            for ch in line[:-1]:
                lines_n[-1].append(int(ch))

        sum_a = 0
        sum_b = 0
        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch == '0':
                    score, rate = get_score(lines_n, i, j)
                    sum_a += score
                    sum_b += rate
        print('Part One: ', sum_a)
        print('Part Two: ', sum_b)


if __name__ == "__main__":
    main()
