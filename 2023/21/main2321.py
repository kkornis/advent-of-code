import copy


def is_good(lines, x, y):
    if x < 0 or x >= len(lines[0]):
        return False
    if y < 0 or y >= len(lines):
        return False
    if lines[x][y] == '#':
        return False
    return True


def step_one(lines, x, y):
    res = set()
    if is_good(lines, x - 1, y):
        res.add((x - 1, y))
    if is_good(lines, x + 1, y):
        res.add((x + 1, y))
    if is_good(lines, x, y - 1):
        res.add((x, y - 1))
    if is_good(lines, x, y + 1):
        res.add((x, y + 1))
    return res


def step(lines, reached: set[tuple[int, int]], prev_reached, newly_reached):
    new_reached = copy.deepcopy(prev_reached)
    for x, y in newly_reached:
        new_reached = new_reached | step_one(lines, x, y)
    return new_reached, reached, new_reached.difference(prev_reached)


def get_semi_frame(x, y, height, width):
    semi_frame = set()
    for i in range(height + 1):
        semi_frame.add((i, width - y))
    for j in range(width + 1):
        semi_frame.add((height - x, j))
    return semi_frame


def quadratic_summarize(param: int):
    return int(((param + 1) / 2) ** 2)


def main_b(n_steps):
    max_reachable = [[7418, 7394], [7393, 7419]]
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [list(x[:-1]) for x in lines]

        width = len(lines[0])
        height = len(lines)
        assert width == height
        sum_b = 0
        n_max_side = int(n_steps / width) + 1

        for i in range(height):
            assert lines[i][65] != '#'
        for i in range(width):
            assert lines[65][i] != '#'

        field_1 = [['.'] * 131] + lines[66:] + lines[:65] + [['.'] * 131]
        field = []
        for line in field_1:
            field.append(['.'] + line[66:] + line[:65] + ['.'])

        for x, y in [(0, 0), (0, width), (height, 0), (height, width)]:
            print('corner: ', x, y)
            go = True
            semi_frame = get_semi_frame(x, y, height, width)
            n_iter = 0
            while go:
                step_number = 65 + n_iter * 131
                reached = {(x, y)}
                prev_reached = set()
                newly_reached = {(x, y)}
                for k in range(step_number):
                    reached, prev_reached, newly_reached = step(field, reached, prev_reached, newly_reached)
                num_reached = len(reached.difference(semi_frame))
                if max_reachable[(x + y) % 2][n_iter % 2] == num_reached:
                    go = False
                sum_b += (n_max_side - n_iter) * num_reached
                n_iter += 1
            sum_b += max_reachable[(x + y) % 2][n_iter % 2] * quadratic_summarize(n_max_side - n_iter)
            sum_b += max_reachable[(x + y) % 2][(n_iter + 1) % 2] * quadratic_summarize(n_max_side - n_iter - 1)

        sum_b -= 2 * (n_steps + 1)

        print('part b: ', sum_b)


def main_a():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [list(x[:-1]) for x in lines]

        reached = set()
        prev_reached = set()
        newly_reached = set()
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == 'S':
                    reached.add((i, j))
                    newly_reached.add((i, j))

        for i in range(64):
            reached, prev_reached, newly_reached = step(lines, reached, prev_reached, newly_reached)

        print('part a: ', len(reached))


if __name__ == "__main__":
    main_a()
    main_b(26501365)
