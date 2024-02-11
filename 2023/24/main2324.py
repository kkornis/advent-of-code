import pandas as pd
import numpy as np


def add_two_rows(df: pd.DataFrame, line1: tuple, line2: tuple) -> None:
    pos1, vel1 = line1
    pos2, vel2 = line2
    x1, y1, z1 = pos1
    vx1, vy1, vz1 = vel1
    x2, y2, z2 = pos2
    vx2, vy2, vz2 = vel2
    df.loc[len(df.index)] = [vy1 - vy2, vx2 - vx1, 0, y2 - y1, x1 - x2, 0, x2 * vy2 - x1 * vy1 - y2 * vx2 + y1 * vx1]
    df.loc[len(df.index)] = [vz1 - vz2, 0, vx2 - vx1, z2 - z1, 0, x1 - x2, x2 * vz2 - x1 * vz1 - z2 * vx2 + z1 * vx1]


def check_eq(data, result):
    pos1, vel1 = data
    x1, y1, z1 = pos1
    vx1, vy1, vz1 = vel1
    const = 'const'

    print((x1 - result[const][0]) * (vy1 - result[const][4]), (y1 - result[const][1]) * (vx1 - result[const][3]))
    print(result[const][0], result[const][1], result[const][2])


def solve_part_b(data, a, b, c):
    variable_names = ['x', 'y', 'z', 'vx', 'vy', 'vz']
    const = 'const'
    df = pd.DataFrame({nam: [] for nam in variable_names + [const]})
    add_two_rows(df, data[0], data[a])
    add_two_rows(df, data[0], data[b])
    add_two_rows(df, data[0], data[c])

    m = df[variable_names]
    m_inv = pd.DataFrame(np.linalg.inv(m.values))
    result = - m_inv.dot(df[[const]])

    # check_eq(data[a], result)

    return result[const][0] + result[const][1] + result[const][2]


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
        print('ERROR: ', line1, line2)

    else:
        t2 = (a1 - a2) / detv
        t1 = (b1 - b2) / detv
        tx2 = a1 - a2
        tx1 = b1 - b2
        assert -0.1 < detv * pos1[0] + tx1 * vel1[0] - (detv * pos2[0] + tx2 * vel2[0]) < 0.1
        assert -0.1 < detv * pos1[1] + tx1 * vel1[1] - (detv * pos2[1] + tx2 * vel2[1]) < 0.1

        if t1 <= 0 or t2 <= 0:
            return False
        else:
            if 200000000000000 <= pos2[0] + t2 * vel2[0] <= 400000000000000 and \
                    200000000000000 <= pos2[1] + t2 * vel2[1] <= 400000000000000:
                return True
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
        for line1 in data:
            for line2 in data:
                if line1 != line2:
                    if collide_in(line1, line2):
                        sum_a += 1

        part_b = solve_part_b(data, 1, 2, 3)
        print(solve_part_b(data, 1, 2, 3))
        print(solve_part_b(data, 4, 5, 6))
        print(solve_part_b(data, 7, 8, 9))
        print(solve_part_b(data, 10, 11, 12))
        print(solve_part_b(data, 13, 14, 15))
        print(solve_part_b(data, 16, 17, 18))

        print('part a: ', int(sum_a / 2))
        print('part b: ', part_b)


if __name__ == "__main__":
    main()
