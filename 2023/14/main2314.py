import copy


def main_a():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0

        width = len(lines[0]) - 1
        height = len(lines)
        for column_ind in range(width):
            loc_sum = 0
            num_rocks = 0
            for i in range(height):
                ch = lines[height - 1 - i][column_ind]
                if ch == '#':
                    loc_sum += num_rocks * (2 * i - num_rocks + 1) / 2
                    num_rocks = 0
                elif ch == 'O':
                    num_rocks += 1
            loc_sum += num_rocks * (2 * height - num_rocks + 1) / 2
            sum_a += int(loc_sum)

        return sum_a


def roll_north(lines_o: list[list[str]], width: int, height: int) -> tuple[list[list[str]], int]:
    lines = copy.deepcopy(lines_o)
    load = 0
    for column_ind in range(width):
        num_rocks = 0
        for i in range(height):
            ch = lines[height - 1 - i][column_ind]
            if ch == '#':
                load += int(num_rocks * (2 * i - num_rocks + 1) / 2)
                for j in range(num_rocks):
                    lines[height - i + j][column_ind] = 'O'
                    num_rocks = 0
            elif ch == 'O':
                num_rocks += 1
                lines[height - 1 - i][column_ind] = '.'
        load += int(num_rocks * (2 * height - num_rocks + 1) / 2)
        for j in range(num_rocks):
            lines[j][column_ind] = 'O'
    return lines, load


def roll_south(lines_o: list[list[str]], width: int, height: int) -> list[list[str]]:
    lines = copy.deepcopy(lines_o)
    for column_ind in range(width):
        num_rocks = 0
        for i in range(height):
            ch = lines[i][column_ind]
            if ch == '#':
                for j in range(num_rocks):
                    lines[i - j - 1][column_ind] = 'O'
                    num_rocks = 0
            elif ch == 'O':
                num_rocks += 1
                lines[i][column_ind] = '.'
        for j in range(num_rocks):
            lines[height - 1 - j][column_ind] = 'O'
    return lines


def roll_west(lines_o: list[list[str]], width: int) -> list[list[str]]:
    lines = copy.deepcopy(lines_o)
    for line in lines:
        num_rocks = 0
        for i in range(width):
            ch = line[width - 1 - i]
            if ch == '#':
                for j in range(num_rocks):
                    line[width - i + j] = 'O'
                    num_rocks = 0
            elif ch == 'O':
                num_rocks += 1
                line[width - 1 - i] = '.'
        for j in range(num_rocks):
            line[j] = 'O'
    return lines


def roll_east(lines_o: list[list[str]], width: int, height: int) -> tuple[list[list[str]], int]:
    lines = copy.deepcopy(lines_o)
    load = 0
    for k, line in enumerate(lines):
        num_rocks = 0
        for i in range(width):
            ch = line[i]
            if ch == '#':
                for j in range(num_rocks):
                    line[i - j - 1] = 'O'
                    load += num_rocks * (height - k)
                    num_rocks = 0
            elif ch == 'O':
                num_rocks += 1
                line[i] = '.'
        for j in range(num_rocks):
            line[width - 1 - j] = 'O'
        load += num_rocks * (height - k)
    return lines, load


def test1():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        lines = [list(x) for x in lines]
        width = len(lines[0]) - 1
        height = len(lines)
        for k in range(height):
            print(''.join(lines[k]))
        lines, load = roll_north(lines, width, height)
        print(''.join(['=']*200))
        for k in range(height):
            print(''.join(lines[k]))
        print(''.join(['=']*200))
        for _ in range(100):
            lines = roll_south(lines, width, height)
            for k in range(height):
                print(''.join(lines[k]))
            print(''.join(['='] * 200))
            lines, loc_load = roll_north(lines, width, height)
            for k in range(height):
                print(''.join(lines[k]))
            print(''.join(['='] * 200))
            assert load == loc_load


def test2():
    with open('input.txt') as inputtxt:

        lines_raw = inputtxt.readlines()
        lines = [list(x)[:-1] for x in lines_raw]
        width = len(lines[0])
        height = len(lines)
        for k in range(height):
            print(''.join(lines[k]))
        print(''.join(['=']*200))
        lines, load = roll_north(lines, width, height)
        for k in range(height):
            print(''.join(lines[k]))
        print(''.join(['=']*200))
        lines = roll_west(lines, width)
        for k in range(height):
            print(''.join(lines[k]))
        print(''.join(['=']*200))
        lines, _ = roll_east(lines, width, height)
        for k in range(height):
            print(''.join(lines[k]))
        print(''.join(['=']*200))
        lines1, load = roll_north(lines, width, height)
        for _ in range(100):
            lines = roll_west(lines, width)
            lines, _ = roll_east(lines, width, height)
            for k in range(height):
                print(''.join(lines[k]))
            print(''.join(['='] * 200))
            lines1, loc_load = roll_north(lines, width, height)
            for k in range(height):
                print(''.join(lines[k]))
            print(''.join(['='] * 200))
            assert load == loc_load


def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        lines = [list(x)[:-1] for x in lines]
        width = len(lines[0])
        height = len(lines)

        for i in range(1, 161):
            lines, load = roll_north(lines, width, height)
            lines = roll_west(lines, width)
            lines = roll_south(lines, width, height)
            lines, load = roll_east(lines, width, height)
            if i == 126:
                lines126 = lines
        assert lines == lines126
        assert 1000000000 % 34 == 126 % 34
        return load


if __name__ == "__main__":
    print('part a:', main_a())
    print('part b:', main())
