neighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def count_cheats(k, track, height, width, lines):
    n_cheats = 0
    for subj, distance in track.items():
        sx, sy = subj
        for u in range(-k, k + 1):
            for v in range(-k + abs(u), k + 1 - abs(u)):
                cand = (sx + u, sy + v)
                if 0 <= cand[0] < height and 0 <= cand[1] < width:
                    if lines[cand[0]][cand[1]] != '#':
                        assert cand in track, 'Unexpected, not part of track.'
                        if track[cand] - distance >= 100 + abs(u) + abs(v):
                            n_cheats += 1
    return n_cheats


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        height = len(lines)
        width = len(lines[0]) - 1

        for i, line in enumerate(lines):
            if 'S' in line:
                start = (i, line.find('S'))
            if 'E' in line:
                end = (i, line.find('E'))

        track = {start: 0}
        new_places = {start: 0}
        while end not in track and len(new_places) > 0:
            new_new_places = {}
            for new_place, dist in new_places.items():
                npx, npy = new_place
                for nx, ny in neighbours:
                    if lines[npx + nx][npy + ny] != '#' and (npx + nx, npy + ny) not in track:
                        new_new_places[(npx + nx, npy + ny)] = dist + 1
                        track[(npx + nx, npy + ny)] = dist + 1
            new_places = new_new_places

        print('Part One: ', count_cheats(2, track, height, width, lines))
        print('Part Two: ', count_cheats(20, track, height, width, lines))


if __name__ == "__main__":
    main()
