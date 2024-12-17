eps = 1e-2


def main(is_part_two):
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        i = 0
        sum_a = 0
        nndet = 0
        while i < len(lines):
            assert lines[i].startswith('Button A: X+')
            remstr = lines[i][12:]
            a1, a2 = remstr.split(', Y+')

            assert lines[i+1].startswith('Button B: X+')
            remstr = lines[i+1][12:]
            b1, b2 = remstr.split(', Y+')

            assert lines[i+2].startswith('Prize: X=')
            remstr = lines[i+2][9:]
            x1, x2 = remstr.split(', Y=')
            a1 = int(a1)
            a2 = int(a2)
            b1 = int(b1)
            b2 = int(b2)
            x1 = int(x1) + (10000000000000 if is_part_two else 0)
            x2 = int(x2) + (10000000000000 if is_part_two else 0)

            det = a1 * b2 - a2 * b1
            if abs(det) > eps:
                inx11 = b2 / det
                inx12 = -a2 / det
                inx21 = - b1 / det
                inx22 = a1 / det

                assert abs(a1 * inx11 + a2 * inx21 - 1) < 1e-12
                assert abs(a1 * inx12 + a2 * inx22) < 1e-12
                assert abs(b1 * inx11 + b2 * inx21) < 1e-12
                assert abs(b1 * inx12 + b2 * inx22 - 1) < 1e-12

                c1 = inx11 * x1 + inx21 * x2
                c2 = inx12 * x1 + inx22 * x2
                if c1 >= -eps and abs(c1 - int(c1+eps)) < eps and c2 >= -eps and abs(c2 - int(c2+eps)) < eps:
                    # assert c1 < 100 and c2 < 100
                    sum_a += 3 * int(c1 + eps) + int(c2 + eps)

                assert abs(c1 * a1 + c2 * b1 - x1) < eps, c1 * a1 + c2 * b1 - x1
                assert abs(c1 * a2 + c2 * b2 - x2) < eps, c1 * a2 + c2 * b2 - x2

                # assert c1 < 100 and c2 < 100
            else:
                nndet += 1

            i += 4
        assert nndet == 0
        print('Part ' + ('Two: 'if is_part_two else 'One: '), sum_a)


if __name__ == "__main__":
    main(False)
    main(True)
