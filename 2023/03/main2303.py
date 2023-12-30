import re


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        sum_a = 0
        sum_b = 0

        gears = {}

        len_line = len(lines[0]) - 1
        num_lines = len(lines)
        for i, line in enumerate(lines):
            iterable = re.finditer('\\d+', line)
            for match in iterable:
                st = match.start(0)
                en = match.end(0)
                is_adjacent = False
                if i > 0:
                    for t in range(max(0, st - 1), min(len_line, en + 1)):
                        if not (lines[i - 1][t].isdigit() or lines[i - 1][t] == '.'):
                            is_adjacent = True
                        if lines[i - 1][t] == '*':
                            if (i - 1, t) in gears:
                                gears[(i - 1, t)].append(int(match.group(0)))
                            else:
                                gears[(i - 1, t)] = [int(match.group(0))]
                if i < num_lines - 1:
                    for t in range(max(0, st - 1), min(len_line, en + 1)):
                        if not (lines[i + 1][t].isdigit() or lines[i + 1][t] == '.'):
                            is_adjacent = True
                        if lines[i + 1][t] == '*':
                            if (i + 1, t) in gears:
                                gears[(i + 1, t)].append(int(match.group(0)))
                            else:
                                gears[(i + 1, t)] = [int(match.group(0))]
                if st > 0:
                    if not (line[st - 1].isdigit() or line[st - 1] == '.'):
                        is_adjacent = True
                    if line[st - 1] == '*':
                        if (i, st - 1) in gears:
                            gears[(i, st - 1)].append(int(match.group(0)))
                        else:
                            gears[(i, st - 1)] = [int(match.group(0))]
                if en < len_line:
                    if not (line[en].isdigit() or line[en] == '.'):
                        is_adjacent = True
                    if line[en] == '*':
                        if (i, en) in gears:
                            gears[(i, en)].append(int(match.group(0)))
                        else:
                            gears[(i, en)] = [int(match.group(0))]
                if is_adjacent:
                    sum_a += int(match.group(0))

        for gear_l in gears.values():
            if len(gear_l) == 2:
                sum_b += gear_l[0] * gear_l[1]

        print('part a:', sum_a)
        print('part b:', sum_b)


if __name__ == "__main__":
    main()
