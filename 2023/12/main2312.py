def main(part_b):
    with open('input.txt') as inputtxt:
        sum_a = 0

        for line in inputtxt.readlines():
            code, numbers_part = line[:-1].split()
            groups = [int(x) for x in numbers_part.split(',')]
            if part_b:
                code = '?'.join([code] * 5)
                groups = groups * 5

            solution_table = [[]]
            for j in range(len(code) + 1):
                solution_table[0].append(0 if '#' in code[:j] else 1)

            for i, group in enumerate(groups):
                solution_table.append([0])
                for j in range(len(code)):
                    must_end_with = code[j] == '#'

                    fit_end = j + 1 >= group
                    fit_end = fit_end and ('.' not in code[j + 1 - group:j + 1])
                    if j + 1 > group:
                        fit_end = fit_end and code[j - group] != '#'

                    local_res = 0
                    if fit_end:
                        l_ind = max(0, j + 1 - group - 1)
                        local_res += solution_table[i][l_ind]
                    if not must_end_with:
                        local_res += solution_table[i + 1][j]

                    solution_table[i + 1].append(local_res)

            sum_a += solution_table[len(groups)][len(code)]
        return sum_a


if __name__ == "__main__":
    print('part a: ', main(False))
    print('part b: ', main(True))
