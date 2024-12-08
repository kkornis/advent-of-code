import re

NAME = 'XMAS'
NAME_REV = NAME[::-1]


def main_a():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        width = len(lines[0])
        height = len(lines)

        sum_vertical = 0
        sum_horizontal = 0
        sum_diagonal_1 = 0
        sum_diagonal_2 = 0
        for line in lines:
            sum_vertical += len(re.findall(NAME, line))
            sum_vertical += len(re.findall(NAME_REV, line))

        # sum_horizontal
        for i in range(width):
            for j in range(height - 3):
                match = True
                for ind, k in enumerate(NAME):
                    if lines[j + ind][i] != k:
                        match = False
                if match:
                    sum_horizontal += 1
                match = True
                for ind, k in enumerate(NAME_REV):
                    if lines[j + ind][i] != k:
                        match = False
                if match:
                    sum_horizontal += 1

        # sum_diagonal_1
        for i in range(width - 3):
            for j in range(height - 3):
                match = True
                for ind, k in enumerate(NAME):
                    if lines[j + ind][i + ind] != k:
                        match = False
                if match:
                    sum_diagonal_1 += 1
                match = True
                for ind, k in enumerate(NAME_REV):
                    if lines[j + ind][i + ind] != k:
                        match = False
                if match:
                    sum_diagonal_1 += 1

        # sum_diagonal_2
        for i in range(width - 3):
            for j in range(height - 3):
                match = True
                for ind, k in enumerate(NAME):
                    if lines[j + 3 - ind][i + ind] != k:
                        match = False
                if match:
                    sum_diagonal_2 += 1
                match = True
                for ind, k in enumerate(NAME_REV):
                    if lines[j + 3 - ind][i + ind] != k:
                        match = False
                if match:
                    sum_diagonal_2 += 1

        print('part a: ', sum_vertical + sum_horizontal + sum_diagonal_1 + sum_diagonal_2)


def main_b():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        width = len(lines[0])
        height = len(lines)

        summ = 0

        for i in range(width - 2):
            for j in range(height - 2):
                if lines[j + 1][i + 1] == 'A':
                    if (lines[j][i] == 'M' and lines[j + 2][i + 2] == 'S') or (
                            lines[j][i] == 'S' and lines[j + 2][i + 2] == 'M'):
                        if (lines[j][i + 2] == 'M' and lines[j + 2][i] == 'S') or (
                                lines[j][i + 2] == 'S' and lines[j + 2][i] == 'M'):
                            summ += 1

        print('part b: ', summ)


def main():
    main_a()
    main_b()


if __name__ == "__main__":
    main()
