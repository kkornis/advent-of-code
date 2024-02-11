class Routes:
    def __init__(self):
        with open('input.txt') as inputtxt:

            lines = inputtxt.readlines()
            lines = [x[:-1] for x in lines]
            self.width = len(lines[0]) - 2
            self.height = len(lines) - 2
            field = []

            self.up = []
            self.do = []
            self.ri = []
            self.le = []

            for i, line in enumerate(lines[1: -1]):
                field.append(line[1: -1])
                for j in range(len(line[1: -1])):
                    ch = line[j + 1]
                    if ch == '>':
                        self.ri.append((i, j))
                    elif ch == '<':
                        self.le.append((i, j))
                    elif ch == 'v':
                        self.do.append((i, j))
                    elif ch == '^':
                        self.up.append((i, j))
                    else:
                        assert ch == '.'
            self.wall = set()

    def setup_wall(self):
        for i in range(self.height):
            self.wall.add((i, -1))
            self.wall.add((i, self.width))
        for i in range(self.width):
            self.wall.add((-1, i))
            self.wall.add((self.height, i))

    def one_route(self, i, start, end):
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
            for x in self.ri:
                obstacles.add((x[0], (x[1] + i) % self.width))
            for x in self.le:
                obstacles.add((x[0], (x[1] - i) % self.width))
            for x in self.up:
                obstacles.add(((x[0] - i) % self.height, x[1]))
            for x in self.do:
                obstacles.add(((x[0] + i) % self.height, x[1]))

            reached = new_reached - obstacles - self.wall
        i += 1
        return i


def main():
    field = Routes()
    field.setup_wall()

    n_steps = 0
    n_steps = field.one_route(n_steps, (0, 0), (field.height - 1, field.width - 1))
    print('sol a: ', n_steps)
    n_steps = field.one_route(n_steps, (field.height - 1, field.width - 1), (0, 0))
    n_steps = field.one_route(n_steps, (0, 0), (field.height - 1, field.width - 1))
    print('sol b: ', n_steps)


if __name__ == "__main__":
    main()
