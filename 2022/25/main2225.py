def decode(line: str) -> int:
    len_str = len(line)
    fp = 1
    res = 0
    for i in range(len_str):
        ch = line[len_str - 1 - i]
        if ch == '0':
            pass
        elif ch == '1':
            res += fp
        elif ch == '2':
            res += 2 * fp
        elif ch == '=':
            res -= 2 * fp
        elif ch == '-':
            res -= fp
        fp *= 5
    return res


def encode(sum_a: int) -> str:
    if sum_a == 0:
        return ''
    mod5 = sum_a % 5
    if mod5 == 0:
        ch = '0'
    elif mod5 == 1:
        ch = '1'
    elif mod5 == 2:
        ch = '2'
    elif mod5 == 3:
        ch = '='
    elif mod5 == 4:
        ch = '-'
    else:
        raise ValueError
    return encode(int((sum_a + 2) / 5)) + ch


def main():
    with open('input.txt') as inputtxt:

        sum_a = 0

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]

        for line in lines:
            sum_a += decode(line)
        print(encode(sum_a))


if __name__ == "__main__":
    main()
