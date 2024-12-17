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


# directions: 0: east, 1: north, 2: west, 3: south
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
        graph: dict[tuple[int, int, int], tuple[list[tuple[int, int, int]], int]] = {}
        potentials: set[tuple[int, int, int]] = {start}
        graph[start] = ([], 0)
        go = True
        while go and all([x not in graph for x in end]):
            if len(graph) % 100 == 0:
                print(len(graph))
            candidates = []
            remove_l = []
            for v in potentials:
                x, y, dire = v
                nxt1 = step(x, y, dire)
                nx, ny, nd = nxt1
                if lines[nx][ny] != '#' and nxt1 not in graph:
                    candidates.append((nxt1, (v, graph[v][1] + 1)))
                nxt2 = turn_right(x, y, dire)
                if nxt2 not in graph:
                    candidates.append((nxt2, (v, graph[v][1] + 1000)))
                nxt3 = turn_left(x, y, dire)
                if nxt3 not in graph:
                    candidates.append((nxt3, (v, graph[v][1] + 1000)))
                if nxt1 in graph and nxt2 in graph and nxt3 in graph:
                    remove_l.append(v)
            for r in remove_l:
                potentials.remove(r)

            if len(candidates) == 0:
                go = False
            min_value = min([cand[1][1] for cand in candidates])
            for candidate in candidates:
                if candidate[1][1] == min_value:
                    if candidate[0] not in graph:
                        graph[candidate[0]] = ([candidate[1][0]], candidate[1][1])
                    else:
                        graph[candidate[0]][0].append(candidate[1][0])
                    potentials.add(candidate[0])

        assert not all([x not in graph for x in end])
        novelties: set[tuple[int, int, int]] = set()
        min_p_s: set[tuple[int, int]] = {(end[0][0], end[0][1])}
        for x in end:
            if x in graph:
                print('Part One: ', graph[x][1])
                novelties.add(x)

        while len(novelties) > 0:
            new_novelties: set[tuple[int, int, int]] = set()
            for novelty in novelties:
                for ancestor in graph[novelty][0]:
                    new_novelties.add(ancestor)
                    min_p_s.add((ancestor[0], ancestor[1]))
            novelties = new_novelties

        print('Part Two: ', len(min_p_s))


if __name__ == "__main__":
    main()
