def calc_state(seconds: int, states, width, height):
    sum_tl = 0
    sum_tr = 0
    sum_bl = 0
    sum_br = 0

    field = [[0] * width for _ in range(height)]
    for x, y, vx, vy in states:
        cx = (x + seconds * vx) % width
        cy = (y + seconds * vy) % height
        if cx < (width - 1) / 2:
            if cy < (height - 1) / 2:
                sum_tl += 1
            elif cy > (height - 1) / 2:
                sum_tr += 1
        elif cx > (width - 1) / 2:
            if cy < (height - 1) / 2:
                sum_bl += 1
            elif cy > (height - 1) / 2:
                sum_br += 1

        field[cy][cx] = 1

    adjacency = 0
    for i, fl in enumerate(field):
        for j, ch in enumerate(fl):
            if ch > 0:
                ne = -ch
                for k in range(max(0, i - 2), min(height - 1, i + 2) + 1):
                    for q in range(max(0, j - 2), min(width - 1, j + 2) + 1):
                        ne += field[k][q]
                adjacency += ne * ch
    # for l in field:
    #     print("".join([str(x) for x in l]))
    return sum_tl * sum_tr * sum_bl * sum_br, adjacency


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        height = 103  # second coordinate
        width = 101

        states = []
        for line in lines:
            # states.append([[int(y) for y in x[2:].split(',')] for x in line.split(' ')])
            posi_s, velo_s = line.split(' ')
            posi_x_s, posi_y_s = posi_s[2:].split(',')
            velo_x_s, velo_y_s = velo_s[2:].split(',')
            states.append((int(posi_x_s), int(posi_y_s), int(velo_x_s), int(velo_y_s)))
        sum_a, _ = calc_state(100, states, width, height)
        max_adjacency = -1
        madji_ind = None
        for seconds in range(10403):
            _, adjacency = calc_state(seconds, states, width, height)
            if max_adjacency < adjacency:
                max_adjacency = adjacency
                madji_ind = seconds
        print("Part One: ", sum_a)
        print("Part Two: ", madji_ind)


if __name__ == "__main__":
    main()
