
def main():
    unfold = True
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0

        for l_num, line in enumerate(lines):
            code, numbers_part = line[:-1].split()
            numbers = [int(x) for x in numbers_part.split(',')]
            if unfold:
                code = '?'.join([code] * 5)
                numbers = numbers * 5

            len_code = len(code)

            solution_table = [[]]
            for j in range(len(code) + 1):
                if '#' in code[len_code - j:]:
                    solution_table[0].append(0)
                else:
                    solution_table[0].append(1)

            for i in range(1, len(numbers) + 1):
                solution_table.append([0])
                for j in range(1, len(code) + 1):
                    must_start_with = code[len_code - j] == '#'

                    fit_start = j >= numbers[len(numbers) - i]
                    fit_start = fit_start and ('.' not in code[len_code - j: len_code - j + numbers[len(numbers) - i]])
                    if len_code > len_code - j + numbers[len(numbers) - i]:
                        fit_start = fit_start and code[len_code - j + numbers[len(numbers) - i]] != '#'

                    local_res = 0
                    if fit_start:
                        l_ind = max(0, j - numbers[len(numbers) - i] - 1)
                        local_res += solution_table[i - 1][l_ind]
                    if not must_start_with:
                        local_res += solution_table[i][j - 1]

                    solution_table[i].append(local_res)

            sum_a += solution_table[len(numbers)][len(code)]
        print(sum_a)


if __name__ == "__main__":
    main()
