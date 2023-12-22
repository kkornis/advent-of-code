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

    def is_above_each_other(self, other):
        return (is_intersection(self.x_start, self.x_end, other.x_start, other.x_end) and
                is_intersection(self.y_start, self.y_end, other.y_start, other.y_end))

    def is_bellow(self, other) -> bool:
        if self.z_end > other.z_start:
            return False
        return self.is_above_each_other(other)


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]

        bricks: list[Brick] = []
        for line in lines:
            bricks.append(Brick(line))

        num_fallen = 0
        while any([not brick.fallen for brick in bricks]) > 0:
            print(num_fallen)
            i = 0
            go = True
            while go:
                if not bricks[i].fallen:
                    if all([(brick.fallen or (not brick.is_bellow(bricks[i])) or (brick is bricks[i])) for brick in bricks]):
                        go = False
                if go:
                    i += 1
            new_z = min([fallen.z_end for fallen in bricks if fallen.is_bellow(bricks[i]) and fallen.fallen], default=0)
            bricks[i].z_end = bricks[i].z_end - bricks[i].z_start + new_z
            bricks[i].z_start = new_z
            bricks[i].fallen = True
            num_fallen += 1

        sum_a = 0

        print('part a: ', sum_a)


if __name__ == "__main__":
    main()
