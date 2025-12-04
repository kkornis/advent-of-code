def calc_p_a(i, j, inp, width, height):
    ret = 0
    for p in [-1, 0, 1]:
        for q in [-1, 0, 1]:
            if p == 0 and q == 0:
                pass
            else:
                s = i + p
                t = j + q
                if s < 0 or s >= height or t < 0 or t >= width:
                    pass
                else:
                    if inp[s][t] == '@':
                        ret += 1
    return ret


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        sum_a = 0
        sum_b = 0
        inp = []
        for line in lines:
            inp.append(line[:-1])

        width = len(inp[0])
        height = len(inp)
        for i in range(height):
            for j in range(width):
                if inp[i][j] == '@' and calc_p_a(i, j, inp, width, height) < 4:
                    sum_a += 1
                    print(i, j, calc_p_a(i, j, inp, width, height))

        print('Part One: ', sum_a)
        print('Part One: ', sum_b)


if __name__ == "__main__":
    main()
