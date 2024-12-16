def step(x, y, dire):
    if dire == 0:
        return x, y + 1, dire
    elif dire == 1:
        return x - 1, y, dire
    elif dire == 2:
        return x, y - 1, dire
    elif dire == 3:
        return x + 1, y, dire


def turn_right(x, y, dire):
    return x, y, (dire - 1) % 4


def turn_left(x, y, dire):
    return x, y, (dire + 1) % 4


# directions: 0: east, 1: north, 2: west, 3: s
def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        start = None
        for i, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch == 'S':
                    start = (i, j, 0)
                elif ch == 'E':
                    end = [(i, j, x) for x in range(4)]
        # from: posi, to parent posi plus score so far
        graph: dict[tuple[int, int, int], tuple[tuple[int, int, int], int]] = {}
        graph[start] = (None, 0)
        new_item = start
        while new_item is not None and all([x not in graph for x in end]):
            if len(graph) % 100 == 0:
                print(len(graph))
            candidates = []
            for v in graph:
                x, y, dire = v
                nxt = step(x, y, dire)
                nx, ny, nd = nxt
                if lines[nx][ny] != '#' and nxt not in graph:
                    candidates.append((nxt, (v, graph[v][1] + 1)))
                nxt = turn_right(x, y, dire)
                if nxt not in graph:
                    candidates.append((nxt, (v, graph[v][1] + 1000)))
                nxt = turn_left(x, y, dire)
                if nxt not in graph:
                    candidates.append((nxt, (v, graph[v][1] + 1000)))

            if len(candidates) == 0:
                new_item = None
            else:
                min_value = candidates[0][1][1]
                min_indx = candidates[0]
                for candidate in candidates:
                    if candidate[1][1] < min_value:
                        min_value = candidate[1][1]
                        min_indx = candidate
                graph[min_indx[0]] = min_indx[1]

        assert not all([x not in graph for x in end])
        for x in end:
            if x in graph:
                print('Part One: ', graph[x][1])


if __name__ == "__main__":
    main()
