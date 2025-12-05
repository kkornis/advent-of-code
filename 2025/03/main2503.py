def calc_segment(line, start_check, right_space):
    argmax = -1
    maxx = -100
    for u in range(start_check, len(line) - right_space):
        if int(line[u]) > maxx:
            maxx = int(line[u])
            argmax = u
    return maxx, argmax


def calc_b(line, n_digits):
    summ = 0
    argmax = -1
    for i in range(n_digits):
        maxx_val, argmax = calc_segment(line, argmax + 1, n_digits - i - 1)
        summ *= 10
        summ += maxx_val
    return summ


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        sum_a = 0
        sum_b = 0
        for line in lines:
            sum_a += calc_b(line[:-1], 2)
            sum_b += calc_b(line[:-1], 12)

        print('Part One: ', sum_a)
        print('Part Two: ', sum_b)


if __name__ == "__main__":
    main()
