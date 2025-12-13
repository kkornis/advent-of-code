from scipy.optimize import linprog


def count_line(buttons, combination):
    a = {tuple((False for _ in range(len(combination))))}
    i = 0
    go = True
    while i < len(combination) and go:
        new_a = set()
        for reachable in a:
            for button in buttons:
                new_a.add(tuple(((x != y) for x, y in zip(button, reachable))))

        a = new_a
        go = combination not in a
        i += 1

    return i


def count_line_b(buttons_l, joltages):
    a_eq = [[int(x in b) for b in buttons_l] for x in range(len(joltages))]
    b_eq = [[x] for x in joltages]

    c = [1 for _ in range(len(buttons_l))]

    res = linprog(c, None, None, a_eq, b_eq, method='highs', integrality=1)

    return int(sum(res.x))


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0

        for line in lines:
            i1 = line.find(']')
            i3 = line.find('{')
            i4 = line.find('}')
            joltages_str = line[i3 + 1:i4]
            joltages = tuple((int(x) for x in joltages_str.split(',')))
            buttons_l = [[int(y) for y in x[1:-1].split(',')] for x in line[i1 + 2: i3 - 1].split()]
            buttons = [tuple((ind in one_button for ind in range(len(joltages)))) for one_button in buttons_l]

            comb_str = line[1:i1]
            combination = tuple((x == '#' for x in comb_str))

            sum_a += count_line(buttons, combination)

            sum_b += count_line_b(buttons_l, joltages)

        print('Part One: ', sum_a)
        print('Part Two: ', sum_b)


if __name__ == "__main__":
    main()
