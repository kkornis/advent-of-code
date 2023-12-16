
def main():
    with open('input.txt') as inputtxt:

        sum_a = 0
        sum_b = 0

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        width = len(lines[0])
        height = len(lines)

        from_left = [[False] * width for i in range(height)]
        from_right = [[False] * width for i in range(height)]
        from_top = [[False] * width for i in range(height)]
        from_bottom = [[False] * width for i in range(height)]

        from_left[0][0] = True

        unhandled = [(0, 0)]
        start = 0
        end = 1

        while end - start > 0:
            x, y = unhandled[0]
            if from_left[x][y]:
                if lines[x][y] == '.':
                    if y + 1 < width:
                        if not from_left[x][y + 1]:
                            from_left[x][y + 1] = True
                            unhandled.append((x, y + 1))
                            end += 1
                elif lines[x][y] == '\\':
                    pass
                elif lines[x][y] == '/':
                    pass
                elif lines[x][y] == '-':
                    pass
                elif lines[x][y] == '|':
                    pass

        print(sum_a)


if __name__ == "__main__":
    main()
