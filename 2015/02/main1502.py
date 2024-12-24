def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0
        for line in lines:
            u = [int(a) for a in line.split('x')]
            assert len(u) == 3
            sum_a += 2 * (u[0] * u[1] + u[1] * u[2] + u[2] * u[0]) + u[0] * u[1] * u[2] // max(u)
            sum_b += u[0] * u[1] * u[2] + 2 * (u[0] + u[1] + u[2] - max(u))
        print(sum_a)
        print(sum_b)


if __name__ == "__main__":
    main()
