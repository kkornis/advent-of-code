def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        height = len(lines)
        width = len(lines[0]) - 1

        frequencies = {}
        for i, line in enumerate(lines):
            for j, ch in enumerate(line[:-1]):
                if ch != '.':
                    if ch in frequencies:
                        frequencies[ch].add((i, j))
                    else:
                        frequencies[ch] = {(i, j)}
        anti_nodes = set()
        anti_nodes_b = set()
        for freq, occ in frequencies.items():
            for fi, fj in occ:
                for si, sj in occ:
                    if fi != si or fj != sj:
                        xi = 2 * fi - si
                        xj = 2 * fj - sj
                        if 0 <= xi < height and 0 <= xj < width:
                            anti_nodes.add((xi, xj))

                        go = True
                        dis = 0
                        while go:
                            xi = (1 + dis) * fi - dis * si
                            xj = (1 + dis) * fj - dis * sj
                            if 0 <= xi < height and 0 <= xj < width:
                                anti_nodes_b.add((xi, xj))
                                dis += 1
                            else:
                                go = False

        print('a: ', len(anti_nodes))
        print('b: ', len(anti_nodes_b))


if __name__ == "__main__":
    main()
