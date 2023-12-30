def decode(line: str) -> int:
    len_str = len(line)
    fp = 1
    res = 0
    for i in range(len_str):
        ch = line[len_str - 1 - i]
        res += fp * {'0': 0, '1': 1, '2': 2, '=': -2, '-': -1}[ch]
        fp *= 5
    return res


def encode(sum_a: int) -> str:
    if sum_a == 0:
        return ''
    mod5 = sum_a % 5
    return encode(int((sum_a + 2) / 5)) + {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}[mod5]


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
