def can_fit_specif(length, width, required_amounts, present_shapes, present_sizes):
    size = length * width

    sumsizes = 0
    for ra, ps in zip(required_amounts, present_sizes):
        sumsizes += ra * ps
    if sumsizes > size:
        return False
    if ((length // 3) * (width // 3)) >= (sum(required_amounts)):
        return True
    else:
        print(1, (length // 3) * (width // 3), sum(required_amounts))
        return None


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        can_fit = 0
        not_fit = 0
        indefinits = 0

        present_shapes = []
        present_sizes = []
        for pr_i in range(6):
            present_shape = []
            present_sizes.append(0)
            for line in lines[5 * pr_i + 1:5 * pr_i + 5]:
                present_shape.append(line[:-1])
                present_sizes[-1] += line.count('#')
            present_shapes.append(present_shape)

        for line in lines[30:]:
            size, amounts = line.split(':')
            length_str, width_str = size.split('x')
            required_amounts = [int(x) for x in amounts.split()]
            code = can_fit_specif(int(length_str), int(width_str), required_amounts, present_shapes, present_sizes)
            if code is None:
                indefinits += 1
            elif code:
                can_fit += 1
            else:
                not_fit += 1

        assert indefinits == 0
        print('Part One: ', can_fit)


if __name__ == "__main__":
    main()
