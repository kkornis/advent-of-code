
def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0
        print(lines[20].find('S'))

        prev_x = 20
        prev_y = 103
        steps = 1
        y = 103
        x = 21
        loop = [(20, 103)]
        while lines[x][y] != 'S':
            loop.append((x, y))
            if lines[x][y] == '|':
                if prev_x == x - 1:
                    prev_x = x
                    prev_y = y
                    x = prev_x + 1
                else:
                    prev_x = x
                    prev_y = y
                    x = prev_x - 1
            elif lines[x][y] == '-':
                if prev_y == y - 1:
                    prev_x = x
                    prev_y = y
                    y = prev_y + 1
                else:
                    prev_x = x
                    prev_y = y
                    y = prev_y - 1
            elif lines[x][y] == 'L':
                if prev_y == y + 1:
                    prev_x = x
                    prev_y = y
                    x = prev_x - 1
                else:
                    prev_x = x
                    prev_y = y
                    y = prev_y + 1
            elif lines[x][y] == 'J':
                if prev_y == y - 1:
                    prev_x = x
                    prev_y = y
                    x = prev_x - 1
                else:
                    prev_x = x
                    prev_y = y
                    y = prev_y - 1
            elif lines[x][y] == 'F':
                if prev_y == y + 1:
                    prev_x = x
                    prev_y = y
                    x = prev_x + 1
                else:
                    prev_x = x
                    prev_y = y
                    y = prev_y + 1
            elif lines[x][y] == '7':
                if prev_y == y - 1:
                    prev_x = x
                    prev_y = y
                    x = prev_x + 1
                else:
                    prev_x = x
                    prev_y = y
                    y = prev_y - 1
            else:
                raise ValueError
            steps += 1

        for i, line in enumerate(lines):
            crossings = 0
            for j, ch in enumerate(line[:-1]):
                if (i, j) in loop:
                    if ch in ['|', 'L', 'J']:
                        crossings += 1
                else:
                    if crossings % 2 == 1:
                        sum_b += 1



        sum_a = steps / 2
        print(sum_a)
        print(sum_b)


if __name__ == "__main__":
    main()


