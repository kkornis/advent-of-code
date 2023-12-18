def one_route(i, height, width, ri, le, up, do, wall, start, end):
    reached = set()
    while end not in reached:
        i += 1
        new_reached = set()
        new_reached.add(start)
        for x in reached:
            new_reached.add(x)
            new_reached.add(((x[0] - 1), x[1]))
            new_reached.add(((x[0] + 1), x[1]))
            new_reached.add((x[0], (x[1] - 1)))
            new_reached.add((x[0], (x[1] + 1)))

        obstacles = set()
        for x in ri:
            obstacles.add((x[0], (x[1] + i) % width))
        for x in le:
            obstacles.add((x[0], (x[1] - i) % width))
        for x in up:
            obstacles.add(((x[0] - i) % height, x[1]))
        for x in do:
            obstacles.add(((x[0] + i) % height, x[1]))

        reached = new_reached - obstacles - wall
    i += 1
    return i


def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        width = len(lines[0]) - 2
        height = len(lines) - 2
        field = []

        up = []
        do = []
        ri = []
        le = []

        for i, line in enumerate(lines[1: -1]):
            field.append(line[1: -1])
            for j in range(len(line[1: -1])):
                ch = line[j + 1]
                if ch == '>':
                    ri.append((i, j))
                elif ch == '<':
                    le.append((i, j))
                elif ch == 'v':
                    do.append((i, j))
                elif ch == '^':
                    up.append((i, j))
                else:
                    assert ch == '.'

        wall = set()
        for i in range(height):
            wall.add((i, -1))
            wall.add((i, width))
        for i in range(width):
            wall.add((-1, i))
            wall.add((height, i))
        n_steps = 0
        n_steps = one_route(n_steps, height, width, ri, le, up, do, wall, (0, 0), (height - 1, width - 1))
        print('sol a: ', n_steps)
        n_steps = one_route(n_steps, height, width, ri, le, up, do, wall, (height - 1, width - 1), (0, 0))
        n_steps = one_route(n_steps, height, width, ri, le, up, do, wall, (0, 0), (height - 1, width - 1))
        print('sol b: ', n_steps)



if __name__ == "__main__":
    main()
