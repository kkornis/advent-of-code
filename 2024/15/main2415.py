def main_a():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        height = None
        moves = ""
        for i, line in enumerate(lines):
            if height is not None:
                moves += line[:-1]
            if line == '\n':
                height = i

        field = [list(x) for x in lines[:height]]
        width = len(lines[0]) - 1
        x = None
        y = None
        for i, line in enumerate(field):
            for j, ch in enumerate(line):
                if ch == '@':
                    x = i
                    y = j

        for move in moves:
            if move == '^':
                k = 0
                while field[x - k - 1][y] == 'O':
                    k += 1
                if field[x - k - 1][y] == '#':
                    pass
                else:
                    field[x - k - 1][y] = 'O'
                    field[x - 1][y] = '.'
                    x -= 1

            elif move == 'v':
                k = 0
                while field[x + k + 1][y] == 'O':
                    k += 1
                if field[x + k + 1][y] == '#':
                    pass
                else:
                    field[x + k + 1][y] = 'O'
                    field[x + 1][y] = '.'
                    x += 1

            elif move == '<':
                k = 0
                while field[x][y - k - 1] == 'O':
                    k += 1
                if field[x][y - k - 1] == '#':
                    pass
                else:
                    field[x][y - k - 1] = 'O'
                    field[x][y - 1] = '.'
                    y -= 1

            elif move == '>':
                k = 0
                while field[x][y + k + 1] == 'O':
                    k += 1
                if field[x][y + k + 1] == '#':
                    pass
                else:
                    field[x][y + k + 1] = 'O'
                    field[x][y + 1] = '.'
                    y += 1

        sum_a = 0
        for i, line in enumerate(field):
            for j, ch in enumerate(line):
                if ch == 'O':
                    sum_a += 100 * i + j

        print('Part one: ', sum_a)


def convert(param: list[str]) -> list[list]:
    ret = []
    for par in param:
        ret.append([])
        for ch in par:
            if ch == '#':
                ret[-1].extend(['#', '#'])
            if ch == '.':
                ret[-1].extend(['.', '.'])
            if ch == '@':
                ret[-1].extend(['@', '.'])
            if ch == 'O':
                ret[-1].extend(['[', ']'])
    return ret


def test(field):
    num = 0
    for line in field:
        for j, ch in enumerate(line):
            if ch == '[':
                num += 1
                assert line[j + 1] == ']'
            elif ch == ']':
                assert line[j - 1] == '['
    # assert num == 21


def main_b():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        height = None
        moves = ""
        for i, line in enumerate(lines):
            if height is not None:
                moves += line[:-1]
            if line == '\n':
                height = i

        field = convert(lines[:height])
        width = len(lines[0]) - 1
        x = None
        y = None
        for i, line in enumerate(field):
            for j, ch in enumerate(line):
                if ch == '@':
                    x = i
                    y = j

        for move in moves:
            if move == '^':
                things_to_move = []
                new_mv_candidates = [(x - 1, y)]
                mv_fails = False
                while len(new_mv_candidates) > 0 and not mv_fails:
                    converted_nmc = new_mv_candidates.copy()
                    for cand in new_mv_candidates:
                        if field[cand[0]][cand[1]] == '[':
                            assert field[cand[0]][cand[1] + 1] == ']'
                            if (cand[0], cand[1] + 1) not in converted_nmc:
                                converted_nmc.append((cand[0], cand[1] + 1))
                        elif field[cand[0]][cand[1]] == ']':
                            assert field[cand[0]][cand[1] - 1] == '['
                            if (cand[0], cand[1] - 1) not in converted_nmc:
                                converted_nmc.append((cand[0], cand[1] - 1))

                    new_mv_candidates = []
                    for cand in converted_nmc:
                        if field[cand[0]][cand[1]] == '#':
                            mv_fails = True
                        elif field[cand[0]][cand[1]] in ['[', ']']:
                            things_to_move.append(cand)
                            new_mv_candidates.append((cand[0] - 1, cand[1]))
                        elif field[cand[0]][cand[1]] == '.':
                            pass
                if not mv_fails:
                    for ttm in reversed(things_to_move):
                        field[ttm[0] - 1][ttm[1]] = field[ttm[0]][ttm[1]]
                        field[ttm[0]][ttm[1]] = '.'
                    x -= 1

            elif move == 'v':
                things_to_move = []
                new_mv_candidates = [(x + 1, y)]
                mv_fails = False
                while len(new_mv_candidates) > 0 and not mv_fails:
                    converted_nmc = new_mv_candidates.copy()
                    for cand in new_mv_candidates:
                        if field[cand[0]][cand[1]] == '[':
                            assert field[cand[0]][cand[1] + 1] == ']'
                            if (cand[0], cand[1] + 1) not in converted_nmc:
                                converted_nmc.append((cand[0], cand[1] + 1))
                        elif field[cand[0]][cand[1]] == ']':
                            assert field[cand[0]][cand[1] - 1] == '['
                            if (cand[0], cand[1] - 1) not in converted_nmc:
                                converted_nmc.append((cand[0], cand[1] - 1))

                    new_mv_candidates = []
                    for cand in converted_nmc:
                        if field[cand[0]][cand[1]] == '#':
                            mv_fails = True
                        elif field[cand[0]][cand[1]] in ['[', ']']:
                            things_to_move.append(cand)
                            new_mv_candidates.append((cand[0] + 1, cand[1]))
                        elif field[cand[0]][cand[1]] == '.':
                            pass
                if not mv_fails:
                    for ttm in reversed(things_to_move):
                        field[ttm[0] + 1][ttm[1]] = field[ttm[0]][ttm[1]]
                        field[ttm[0]][ttm[1]] = '.'
                    x += 1

            elif move == '<':
                k = 0
                while field[x][y - k - 1] in ['[', ']']:
                    k += 1
                if field[x][y - k - 1] == '#':
                    pass
                else:
                    assert k % 2 == 0
                    for i in range(k // 2):
                        field[x][y - i * 2 - 3] = '['
                        field[x][y - i * 2 - 2] = ']'
                    field[x][y - 1] = '.'
                    y -= 1

            elif move == '>':
                k = 0
                while field[x][y + k + 1] in ['[', ']']:
                    k += 1
                if field[x][y + k + 1] == '#':
                    pass
                else:
                    assert k % 2 == 0
                    for i in range(k // 2):
                        field[x][y + i * 2 + 3] = ']'
                        field[x][y + i * 2 + 2] = '['
                    field[x][y + 1] = '.'
                    y += 1
            test(field)

        sum_a = 0
        for i, line in enumerate(field):
            for j, ch in enumerate(line):
                if ch == '[':
                    sum_a += 100 * i + j

        print('Part Two: ', sum_a)


if __name__ == "__main__":
    main_a()
    main_b()
