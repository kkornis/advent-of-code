neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def process_perims(perims: list[tuple[int, int, bool]]) -> int:
    connecteds: list[list[tuple[int, int, bool]]] = []
    for perim in perims:
        xcoo, ycoo, direction = perim
        before_cand_killer = (xcoo, ycoo, not direction)
        if direction:
            after_cand_killer = (xcoo, ycoo + 1, not direction)

            before_cand = (xcoo, ycoo - 1, direction)
            before_cand_ind = None
            for q, comp in enumerate(connecteds):
                if before_cand in comp:
                    before_cand_ind = q
            if before_cand_killer in perims:
                before_cand_ind = None

            after_cand = (xcoo, ycoo + 1, direction)
            after_cand_ind = None
            for q, comp in enumerate(connecteds):
                if after_cand in comp:
                    after_cand_ind = q
            if after_cand_killer in perims:
                after_cand_ind = None

            if before_cand_ind is None and after_cand_ind is None:
                connecteds.append([perim])
            elif before_cand_ind is not None and after_cand_ind is None:
                connecteds[before_cand_ind].append(perim)
            elif before_cand_ind is None and after_cand_ind is not None:
                connecteds[after_cand_ind].append(perim)
            elif before_cand_ind is not None and after_cand_ind is not None:
                connecteds[before_cand_ind].append(perim)
                tmp = connecteds[after_cand_ind]
                connecteds[before_cand_ind].extend(tmp)
                connecteds.pop(after_cand_ind)
            else:
                raise Exception

        else:
            after_cand_killer = (xcoo + 1, ycoo, not direction)

            before_cand = (xcoo - 1, ycoo, direction)
            before_cand_ind = None
            for q, comp in enumerate(connecteds):
                if before_cand in comp:
                    before_cand_ind = q
            if before_cand_killer in perims:
                before_cand_ind = None

            after_cand = (xcoo + 1, ycoo, direction)
            after_cand_ind = None
            for q, comp in enumerate(connecteds):
                if after_cand in comp:
                    after_cand_ind = q
            if after_cand_killer in perims:
                after_cand_ind = None

            if before_cand_ind is None and after_cand_ind is None:
                connecteds.append([perim])
            elif before_cand_ind is not None and after_cand_ind is None:
                connecteds[before_cand_ind].append(perim)
            elif before_cand_ind is None and after_cand_ind is not None:
                connecteds[after_cand_ind].append(perim)
            elif before_cand_ind is not None and after_cand_ind is not None:
                connecteds[before_cand_ind].append(perim)
                tmp = connecteds[after_cand_ind]
                connecteds[before_cand_ind].extend(tmp)
                connecteds.pop(after_cand_ind)
            else:
                raise Exception

    return len(connecteds)


def process_region(lines, i, j):
    height = len(lines)
    width = len(lines[0]) - 1
    ch = lines[i][j]
    perimeter = 0
    perims: list[tuple[int, int, bool]] = []
    plants = [(i, j)]
    new_plants = [(i, j)]
    while len(new_plants) > 0:
        new_new_plants = []
        for x, y in new_plants:
            for nxa, nya in neighbours:
                cand = (x + nxa, y + nya)
                if 0 <= cand[0] < height and 0 <= cand[1] < width and lines[cand[0]][cand[1]] == ch:
                    if cand not in plants and cand not in new_new_plants:
                        new_new_plants.append(cand)
                else:
                    perimeter += 1
                    direction = bool(abs(nxa))
                    xcoo = x
                    if nxa == 1:
                        xcoo += 1
                    ycoo = y
                    if nya == 1:
                        ycoo += 1
                    perims.append((xcoo, ycoo, direction))
        new_plants = new_new_plants
        plants.extend(new_plants)

    return [plants, perimeter, process_perims(perims)]


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        # The outer list has length 3, contains i the set of plants, ii the area, and iii ...
        regions: list[list[list[tuple[int, int]], int, int]] = []
        for i, line in enumerate(lines):
            for j, ch in enumerate(line[:-1]):
                if not any([(i, j) in reg[0] for reg in regions]):
                    regions.append(process_region(lines, i, j))

        sum_a = 0
        sum_b = 0
        for reg_data in regions:
            assert len(reg_data) == 3
            sum_a += reg_data[1] * len(reg_data[0])
            sum_b += reg_data[2] * len(reg_data[0])
        print('Part One: ', sum_a)
        print('Part Two: ', sum_b)


if __name__ == "__main__":
    main()
