def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        pos = None
        for i, line in enumerate(lines):
            if '^' in line:
                pos = (i, line.find('^'), 0)

        _, visits = is_stuck(pos, lines)

        visits_s = {(visit[0], visit[1]) for visit in visits}
        print('part a: ', len(visits_s))

        sum_b = 0
        for i, j in visits_s:
            if i == pos[0] and j == pos[1]:
                continue
            alt_lines = lines.copy()
            alt_lines[i] = lines[i][:j] + '#' + lines[i][j+1:]
            stuck, _ = is_stuck(pos, alt_lines)
            sum_b += int(stuck)

        print('part b: ', sum_b)


def is_stuck(pos, lines):
    height = len(lines)
    width = len(lines[0]) - 1

    visits = {pos}

    m1 = {0: -1, 1: 0, 2: 1, 3: 0}
    m2 = {0: 0, 1: 1, 2: 0, 3: -1}
    while True:
        next_cand = (pos[0] + m1[pos[2]], pos[1] + m2[pos[2]], pos[2])

        if not (0 <= next_cand[0] < height and 0 <= next_cand[1] < width):
            return False, visits

        if lines[next_cand[0]][next_cand[1]] == '#':
            new_dir = (pos[2] + 1) % 4
            pos = (pos[0], pos[1], new_dir)
        else:
            pos = next_cand

        if pos in visits:
            return True, visits
        visits.add(pos)


if __name__ == "__main__":
    main()
