
def main(part_b):
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0

        for l_num, line in enumerate(lines):
            code, numbers_part = line[:-1].split()
            numbers = [int(x) for x in numbers_part.split(',')]
            if part_b:
                code = '?'.join([code] * 5)
                numbers = numbers * 5

            len_code = len(code)

            solution_table = [[]]
            for j in range(len(code) + 1):
                if '#' in code[:j]:
                    solution_table[0].append(0)
                else:
                    solution_table[0].append(1)

            for i in range(len(numbers)):
                solution_table.append([0])
                for j in range(len_code):
                    must_ends_with = code[j] == '#'

                    fit_end = j + 1 >= numbers[i]
                    fit_end = fit_end and ('.' not in code[j + 1 - numbers[i]:j + 1])
                    if j + 1 > numbers[i]:
                        fit_end = fit_end and code[j - numbers[i]] != '#'

                    local_res = 0
                    if fit_end:
                        l_ind = max(0, j + 1 - numbers[i] - 1)
                        local_res += solution_table[i][l_ind]
                    if not must_ends_with:
                        local_res += solution_table[i + 1][j]

                    solution_table[i + 1].append(local_res)

            sum_a += solution_table[len(numbers)][len(code)]
        return sum_a


if __name__ == "__main__":
    print('part a: ', main(False))
    print('part b: ', main(True))
