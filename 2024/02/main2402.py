def is_safe_a(x: list[int]):
    safes = {-3, -2, -1, 1, 2, 3}
    safe = True
    for ind in range(1, len(x)):
        if x[ind] - x[ind - 1] not in safes or (x[ind] - x[ind - 1]) * (x[1] - x[0]) < 0:
            safe = False
    return safe


def is_safe_b(x: list[int]):
    assert len(x) > 2
    for i in range(len(x)):
        if is_safe_a(x[:i] + x[i + 1:]):
            return True
    return False


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        counter = 0
        counter_b = 0
        for line in lines:
            proc_line = [int(x) for x in line.split(' ')]
            safe = is_safe_a(proc_line)
            safe_b = is_safe_b(proc_line)
            if safe:
                counter += 1
            if safe_b:
                counter_b += 1
        print('part a: ', counter)
        print('part b: ', counter_b)


if __name__ == "__main__":
    main()
