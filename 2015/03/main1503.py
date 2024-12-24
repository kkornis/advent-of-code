def main():
    with open('input.txt') as inputtxt:
        line = inputtxt.read()

        x = 0
        y = 0
        presents = {(0, 0)}
        for ch in line:
            if ch == '^':
                x += 1
            elif ch == 'v':
                x -= 1
            elif ch == '<':
                y -= 1
            elif ch == '>':
                y += 1
            else:
                raise Exception
            presents.add((x, y))
        print(len(presents))


def main2():
    with open('input.txt') as inputtxt:
        line = inputtxt.read()

        x = 0
        y = 0
        x2 = 0
        y2 = 0
        presents = {(0, 0)}
        for i, ch in enumerate(line):
            if i % 2 == 0:
                if ch == '^':
                    x += 1
                elif ch == 'v':
                    x -= 1
                elif ch == '<':
                    y -= 1
                elif ch == '>':
                    y += 1
            presents.add((x, y))
            if i % 2 == 1:
                if ch == '^':
                    x2 += 1
                elif ch == 'v':
                    x2 -= 1
                elif ch == '<':
                    y2 -= 1
                elif ch == '>':
                    y2 += 1
            presents.add((x2, y2))
        print(len(presents))


if __name__ == "__main__":
    main()
    main2()
