
def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0

        width = len(lines[0]) - 1
        height = len(lines)
        for column_ind in range(width):
            loc_sum = 0
            num_rocks = 0
            for i in range(height):
                ch = lines[height - 1 - i][column_ind]
                if ch == '#':
                    loc_sum += num_rocks * (2 * i - num_rocks + 1) / 2
                    num_rocks = 0
                elif ch == 'O':
                    num_rocks += 1
            loc_sum += num_rocks * (2 * height - num_rocks + 1) / 2
            sum_a += loc_sum

        print(sum_a)
        print(sum_b)


if __name__ == "__main__":
    main()
