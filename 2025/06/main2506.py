import math


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        sum_a = 0
        sum_b = 0
        inp = [line.split() for line in lines]

        for i in range(len(inp[0])):
            loc_numbers = [int(inp[j][i]) for j in range(len(inp) - 1)]
            sum_a += sum(loc_numbers) if inp[-1][i] == '+' else math.prod(loc_numbers)

        height = len(lines) - 1  # 4
        width = len(lines[0]) - 1  # 3750

        ind = 0
        while ind < width:
            block = []
            if lines[height][ind] == '+':
                funct = sum
            else:
                assert lines[height][ind] == '*', lines[height][ind]
                funct = math.prod
            while ind < width and not all([lines[x][ind] == ' ' for x in range(height)]):
                loc = 0
                for i in range(height):
                    if lines[i][ind] != ' ':
                        loc *= 10
                        loc += int(lines[i][ind])
                block.append(loc)
                ind += 1
            sum_b += funct(block)
            ind += 1

        print('Part One: ', sum_a)
        print('Part Two: ', sum_b)


if __name__ == "__main__":
    main()
