def main(extra_space):
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0
        sum_hasht = 0

        for l_num, line in enumerate(lines):
            sum_hasht += line[:-1].count('#')

        l_empty_rows = []
        for i in range(140):
            if lines[i].count('#') == 0:
                l_empty_rows.append(i)

        l_empty_cols = []
        for i in range(140):
            if all([line[i] == '.' for line in lines]):
                l_empty_cols.append(i)

        l_hashtags = []
        l_mod = []

        for l_num, line in enumerate(lines):
            for j, ch in enumerate(line):
                if ch == '#':
                    l_hashtags.append((l_num, j))

        for hashtag in l_hashtags:
            row_addition = sum([x < hashtag[0] for x in l_empty_rows])
            col_addition = sum([x < hashtag[1] for x in l_empty_cols])

            l_mod.append((hashtag[0] + row_addition * extra_space, hashtag[1] + col_addition * extra_space))

        for first in l_mod:
            for second in l_mod:
                sum_a += abs(first[0] - second[0]) + abs(first[1] - second[1])

        sum_a = sum_a / 2
        return int(sum_a)


if __name__ == "__main__":
    print('part a: ', main(1))
    print('part b: ', main(999999))


