def check_ok(i, j, tiles):
    if tiles[j][0] < tiles[i][0]:
        return check_ok(j, i, tiles)

    if tiles[j][0] == tiles[i][0] or tiles[j][1] == tiles[i][1]:
        return False
        # This should not hurt

    if tiles[i][1] < tiles[j][1]:
        prev = tiles[-1]
        for tile in tiles:
            if tiles[i][0] < tile[0] < tiles[j][0] and tiles[i][1] < tile[1] < tiles[j][1]:
                return False

            if tile[0] == prev[0]:
                assert tiles[i][0] < tiles[j][0]
                if tiles[i][0] < tile[0] < tiles[j][0]:
                    if tile[1] <= tiles[i][1] and tiles[j][1] <= prev[1]:
                        return False
                    if prev[1] <= tiles[i][1] and tiles[j][1] <= tile[1]:
                        return False
            else:
                assert tiles[i][1] < tiles[j][1]
                if tiles[i][1] < tile[1] < tiles[j][1]:
                    if tile[0] <= tiles[i][0] and tiles[j][0] <= prev[0]:
                        return False
                    if prev[0] <= tiles[i][0] and tiles[j][0] <= tile[0]:
                        return False
            prev = tile
        return True

    else:
        prev = tiles[-1]
        for tile in tiles:
            if tiles[i][0] < tile[0] < tiles[j][0] and tiles[j][1] < tile[1] < tiles[i][1]:
                return False

            if tile[0] == prev[0]:
                assert tiles[i][0] < tiles[j][0]
                if tiles[i][0] < tile[0] < tiles[j][0]:
                    if tile[1] <= tiles[j][1] and tiles[i][1] <= prev[1]:
                        return False
                    if prev[1] <= tiles[j][1] and tiles[i][1] <= tile[1]:
                        return False
            else:
                assert tiles[j][1] < tiles[i][1]
                if tiles[j][1] < tile[1] < tiles[i][1]:
                    if tile[0] <= tiles[i][0] and tiles[j][0] <= prev[0]:
                        return False
                    if prev[0] <= tiles[i][0] and tiles[j][0] <= tile[0]:
                        return False
            prev = tile
        return True


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        tiles = []
        for line in lines:
            tiles.append([int(x) for x in line.split(',')])

        sum_a = -1
        sum_b = -1
        for i, tile1 in enumerate(tiles):
            for j, tile2 in enumerate(tiles):
                if sum_a < abs((tile1[0] - tile2[0] + 1) * (tile1[1] - tile2[1] + 1)):
                    sum_a = abs((tile1[0] - tile2[0] + 1) * (tile1[1] - tile2[1] + 1))

                if sum_b <= abs((tile1[0] - tile2[0] + 1) * (tile1[1] - tile2[1] + 1)):
                    if check_ok(i, j, tiles):
                        sum_b = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)

        print('Part one: ', sum_a)
        print("Part two: ", sum_b)


if __name__ == "__main__":
    main()
