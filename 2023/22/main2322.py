def is_intersection(x_start, x_end, x_start1, x_end1) -> bool:
    if x_start >= x_end1:
        return False
    if x_start1 >= x_end:
        return False
    return True


class Brick:
    def __init__(self, line: str):
        starts, ends = line.split('~')
        x_start, y_start, z_start = starts.split(',')
        x_end, y_end, z_end = ends.split(',')
        self.x_start = int(x_start)
        self.y_start = int(y_start)
        self.z_start = int(z_start)
        self.x_end = int(x_end) + 1
        self.y_end = int(y_end) + 1
        self.z_end = int(z_end) + 1
        self.fallen = False
        self.lands_on = []

    def is_above_each_other(self, other):
        return (is_intersection(self.x_start, self.x_end, other.x_start, other.x_end) and
                is_intersection(self.y_start, self.y_end, other.y_start, other.y_end))

    def is_bellow(self, other) -> bool:
        if self.z_end > other.z_start:
            return False
        return self.is_above_each_other(other)


def get_n_blocks_would_fall(bricks, j):
    stack = {j}
    go = True
    while go:
        go = False
        for k, brick in enumerate(bricks):
            if k not in stack and len(brick.lands_on) > 0 and all([x in stack for x in brick.lands_on]):
                stack.add(k)
                go = True
    return len(stack) - 1


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]

        bricks: list[Brick] = []
        for line in lines:
            bricks.append(Brick(line))

        num_fallen = 0
        while any([not brick.fallen for brick in bricks]):
            if num_fallen % 100 == 0:
                print(num_fallen, '/ 1222')
            i = 0
            go = True
            while go:
                if not bricks[i].fallen:
                    lands_on = []
                    go = False
                    new_z = 0
                    for j, brick in enumerate(bricks):
                        if brick is not bricks[i]:
                            if brick.is_bellow(bricks[i]):
                                if brick.fallen:
                                    if brick.z_end > new_z:
                                        new_z = brick.z_end
                                        lands_on = [j]
                                    elif brick.z_end == new_z:
                                        lands_on.append(j)
                                else:
                                    go = True
                                    break

                if go:
                    i += 1
            bricks[i].z_end = bricks[i].z_end - bricks[i].z_start + new_z
            bricks[i].z_start = new_z
            bricks[i].fallen = True
            bricks[i].lands_on = lands_on
            num_fallen += 1

        stg_landed_on = set()
        for brick in bricks:
            if len(brick.lands_on) == 1:
                stg_landed_on.add(brick.lands_on[0])

        sum_b = 0
        for j, brick in enumerate(bricks):
            addition = get_n_blocks_would_fall(bricks, j)
            sum_b += addition

        print('part a: ', 1222 - len(stg_landed_on))
        print('part b: ', sum_b)


if __name__ == "__main__":
    main()
