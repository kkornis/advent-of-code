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


def step(lines, reached: set[tuple[int, int]]):
    new_reached = set()
    for x, y in reached:
        new_reached = new_reached | step_one(lines, x, y)
    return new_reached


def main():
    with open('input.txt') as inputtxt:

        sum_a = 0
        sum_b = 0

        lines = inputtxt.readlines()
        lines = [list(x[:-1]) for x in lines]
        width = len(lines[0])
        height = len(lines)

        reached = set()
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == 'S':
                    reached.add((i, j))

        for i in range(64):
            reached = step(lines, reached)

        print('part a: ', len(reached))


if __name__ == "__main__":
    main()
