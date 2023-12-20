
def my_hash(code: str) -> int:
    res = 0
    for i in range(len(code)):
        res += ord(code[i])
        res *= 17
    return res % 256


def main():
    with open('input.txt') as inputtxt:

        sum_a = 0
        sum_b = 0

        lines = inputtxt.readlines()
        line = lines[0][:-1]
        words = line.split(',')

        for word in words:
            sum_a += my_hash(word)

        print(sum_a)

        boxes = [[] for _ in range(256)]
        for word in words:
            if word.endswith('-'):
                code = word[: -1]
                box_num = my_hash(code)
                ind = None
                for i, x in enumerate(boxes[box_num]):
                    if x[0] == code:
                        ind = x
                if ind is not None:
                    boxes[box_num].remove(ind)

            else:
                code, foc_str = word.split('=')
                foc = int(foc_str)
                box_num = my_hash(code)
                is_in = False
                for i, x in enumerate(boxes[box_num]):
                    if x[0] == code:
                        boxes[box_num][i] = (code, foc)
                        is_in = True
                if not is_in:
                    boxes[box_num].append((code, foc))

        for i in range(256):
            for j, x in enumerate(boxes[i]):
                sum_b += (1 + i) * (1 + j) * x[1]
        print(sum_b)


if __name__ == "__main__":
    main()
