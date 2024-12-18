neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def solve_one(width, height, rel_bytes):
    in_pat = {(0, 0): 0}
    new_places = {(0, 0): 0}

    while len(new_places) > 0 and (width - 1, height - 1) not in in_pat:
        new_new_places = {}
        for new_place, dist in new_places.items():
            for n_x, n_y in neighbours:
                cand = new_place[0] + n_x, new_place[1] + n_y
                if cand not in rel_bytes and 0 <= cand[0] < width and 0 <= cand[1] < height and cand not in in_pat:
                    in_pat[cand] = dist + 1
                    new_new_places[cand] = dist + 1
        new_places = new_new_places
    return in_pat[(width - 1, height - 1)] if (width - 1, height - 1) in in_pat else None


def main():
    with open("input.txt") as inputtxt:
        f_bytes = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in inputtxt.readlines()]
        height = 71
        width = 71

        print('Part One: ', solve_one(width, height, f_bytes[:1024]))

        i = 3020
        dist = 0
        while dist is not None:
            dist = solve_one(width, height, f_bytes[:i])
            i += 1

        print('Part Two: ', f_bytes[i - 2])


if __name__ == "__main__":
    main()
