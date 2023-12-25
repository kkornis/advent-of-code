def collide_in(line1, line2):
    pos1, vel1 = line1
    pos2, vel2 = line2

    detv = vel2[0] * vel1[1] - vel2[1] * vel1[0]
    a1 = pos1[0] * vel1[1] - pos1[1] * vel1[0]
    a2 = pos2[0] * vel1[1] - pos2[1] * vel1[0]
    b1 = pos1[0] * vel2[1] - pos1[1] * vel2[0]
    b2 = pos2[0] * vel2[1] - pos2[1] * vel2[0]
    if detv == 0:
        if a1 - a2 != 0:
            return False
        else:
            if vel1[0] != 0:
                ta1 = (pos2[0] - pos1[0]) / vel1[0]
            else:
                ta1 = (pos2[1] - pos2[1]) / vel1[1]

            if vel2[0] != 0:
                ta2 = (pos1[0] - pos2[0]) / vel2[0]
            else:
                ta2 = (pos1[1] - pos2[1]) / vel2[1]

            print(ta1, ta2)
            if ta1 <= 0 and ta2 <= 0:
                return False
            else:
                print('ERROR: ', line1, line2)

    else:
        t2 = (a1 - a2) / detv
        t1 = (b1 - b2) / detv
        if t1 <= 0 or t2 <= 0:
            return False
        else:
            # assert -10 < pos1[0] + t1 * vel1[0] - (pos2[0] + t2 * vel2[0]) < 10
            # assert -10 < pos1[1] + t1 * vel1[1] - (pos2[1] + t2 * vel2[1]) < 10
            if 200000000000000 <= pos2[0] + t2 * vel2[0] <= 400000000000000 and \
                    200000000000000 <= pos2[1] + t2 * vel2[1] <= 400000000000000:
                return True
            else:
                return False


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        data = []
        for line in lines:
            a, b = line.split(' @ ')
            data.append(([int(x) for x in a.split(', ')], [int(x) for x in b.split(', ')]))

        sum_a = 0
        sum_b = 0
        for line1 in data:
            for line2 in data:
                if line1 != line2:
                    if collide_in(line1, line2):
                        sum_a += 1

        print('part a: ', int(sum_a / 2))
        print('part b: ', sum_b)


if __name__ == "__main__":
    main()
