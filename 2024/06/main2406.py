def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        height = len(lines)
        width = len(lines[0]) - 1

        pos = None
        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch == '^':
                    pos = (i, j, 0)

        _, visits = is_stuck(pos, lines)
        visits_s = set()
        for visit in visits:
            visits_s.add((visit[0], visit[1]))
        print('part a: ', len(visits_s))

        sum_b = 0
        for i in range(height):
            print('line ' + str(i))
            for j in range(width):
                if not (i == pos[0] and j == pos[1]):
                    alt_lines = lines.copy()
                    alt_lines[i] = lines[i][:j] + '#' + lines[i][j+1:]
                    stuck, visits = is_stuck(pos, alt_lines)
                    if stuck:
                        sum_b += 1

        print('part b: ', sum_b)


def is_stuck(pos, lines):
    height = len(lines)
    width = len(lines[0]) - 1

    visits = {pos}

    go = True
    stuck = False
    while go:
        if pos[2] == 0:
            next_cand = (pos[0] - 1, pos[1], pos[2])
        elif pos[2] == 1:
            next_cand = (pos[0], pos[1] + 1, pos[2])
        elif pos[2] == 2:
            next_cand = (pos[0] + 1, pos[1], pos[2])
        elif pos[2] == 3:
            next_cand = (pos[0], pos[1] - 1, pos[2])
        else:
            raise Exception

        if not (0 <= next_cand[0] < height and 0 <= next_cand[1] < width):
            go = False

        if go:
            if lines[next_cand[0]][next_cand[1]] == '#':
                if pos[2] == 0:
                    pos = (pos[0], pos[1], 1)
                elif pos[2] == 1:
                    pos = (pos[0], pos[1], 2)
                elif pos[2] == 2:
                    pos = (pos[0], pos[1], 3)
                elif pos[2] == 3:
                    pos = (pos[0], pos[1], 0)
                else:
                    raise Exception
            else:
                pos = next_cand

            if pos in visits:
                stuck = True
                go = False
            else:
                visits.add(pos)

    return stuck, visits


if __name__ == "__main__":
    main()
