neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def main():
    with open("input.txt") as inputtxt:
        f_bytes = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in inputtxt.readlines()]
        print(len(f_bytes))
        for f_b in f_bytes:
            assert 2 == len(f_b)

        height = 71
        width = 71
        i = 1024
        # go = True
        # while go:
        rel_bytes = f_bytes[:1024]
        # height = 7
        # width = 7
        # rel_bytes = f_bytes[:12]

        in_pat = {(0, 0): (None, 0)}
        new_places = {(0, 0): (None, 0)}

        while len(new_places) > 0 and (70, 70) not in in_pat:
            new_new_places = {}
            for new_place, dist in new_places.items():
                if new_place == (6, 0):
                    print('x')
                for n_x, n_y in neighbours:
                    cand = new_place[0] + n_x, new_place[1] + n_y
                    if cand not in rel_bytes and 0 <= cand[0] < width and 0 <= cand[1] < height and cand not in in_pat:
                        in_pat[cand] = (new_place, dist[1] + 1)
                        new_new_places[cand] = (new_place, dist[1] + 1)
            new_places = new_new_places

        print('Part One: ', in_pat[(width - 1, height - 1)][1])

        # x = (width - 1, height - 1)
        # while x != (0, 0):
        #     x, dist = in_pat[x]
        #     print(x, dist)
        # print('')


if __name__ == "__main__":
    main()
