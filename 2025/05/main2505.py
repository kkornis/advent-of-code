def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        ranges = [[int(x) for x in line.split('-')] for line in lines if '-' in line]
        ids = [int(line) for line in lines if ('-' not in line and len(line) > 1)]

        ordered = sorted(ranges, key=lambda range__: range__[0])

        i = 0
        while i < len(ordered) - 1:
            if ordered[i][1] >= ordered[i + 1][0]:
                ordered[i] = [ordered[i][0], max(ordered[i + 1][1], ordered[i][1])]
                ordered.pop(i + 1)
            else:
                i += 1

        print('Part One: ', sum([any([range_[0] <= id_ <= range_[1] for range_ in ranges]) for id_ in ids]))
        print('Part Two: ', sum([ord[1] - ord[0] + 1 for ord in ordered]))


if __name__ == "__main__":
    main()
