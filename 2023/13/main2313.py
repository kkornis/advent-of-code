def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0

        start = 0
        end = start

        n_boxes = 0
        while start < len(lines):
            while end < len(lines) and lines[end] != '\n':
                end += 1

            n_boxes += 1

            width = len(lines[start]) - 1

            for i in range(1, end - start):
                is_refl = True
                smudges = 0
                for j in range(0, min(i - 1, end - start - i - 1) + 1):
                    for u in range(width):
                        if lines[start + i - j - 1][u] != lines[start + i + j][u]:
                            smudges += 1
                    if lines[start + i - j - 1] != lines[start + i + j]:
                        is_refl = False
                if is_refl:
                    sum_a += 100 * i
                if smudges == 1:
                    sum_b += 100 * i

            for k in range(1, width):
                is_refl = True
                smudges = 0
                for j in range(0, min(k - 1, width - k - 1) + 1):
                    for t in range(start, end):
                        if lines[t][k - j - 1] != lines[t][k + j]:
                            is_refl = False
                            smudges += 1
                if is_refl:
                    sum_a += k
                if smudges == 1:
                    sum_b += k

            start = end + 1
            end = start

        print(sum_a)
        print(sum_b)


if __name__ == "__main__":
    main()


