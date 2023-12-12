

def main():
    unfold = True
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0

        for l_num, line in enumerate(lines):
            print(l_num)
            code, numbers_part = line[:-1].split()
            numbers = [int(x) for x in numbers_part.split(',')]
            if unfold:
                code = '?'.join([code] * 5)
                numbers = numbers * 5
                print(code)
                print(numbers)

            assert len(numbers) > 0

            len_code = len(code)
            contig_st = []
            sum_x = 0
            go = True
            try_it = True  # if true, try to fix the current state, if false take up one

            while go:
                ind = len(contig_st)
                if ind == len(numbers):
                    if '#' not in code[contig_st[-1] + numbers[ind - 1]:]:
                        sum_x += 1
                    try_it = False
                if try_it:
                    if len(contig_st) > 0:
                        k = contig_st[-1] + numbers[ind - 1] + 1
                    else:
                        k = 0

                    go_in = True
                    try_it = True
                    while go_in:
                        if k + numbers[ind] > len_code or (k > 0 and code[k - 1] == '#'):
                            go_in = False
                            try_it = False
                        else:
                            if '.' in code[k: k + numbers[ind]]:
                                k += 1
                                go_in = True
                            elif k + numbers[ind] < len_code and code[k + numbers[ind]] == '#':
                                k += 1
                                go_in = True
                            elif code[k + numbers[ind]:].count('#') > sum(contig_st[ind + 1:]):
                                k += 1
                                go_in = True
                            else:
                                go_in = False

                    if try_it:
                        contig_st.append(k)
                        try_it = True
                else:
                    if len(contig_st) == 0:
                        go = False
                    else:
                        k = contig_st[-1] + 1
                        contig_st = contig_st[:-1]
                        ind = len(contig_st)

                        go_in = True
                        try_it = True
                        while go_in:
                            if k + numbers[ind] > len_code or (k > 0 and code[k - 1] == '#'):
                                go_in = False
                                try_it = False
                            else:
                                if '.' in code[k: k + numbers[ind]]:
                                    k += 1
                                    go_in = True
                                elif k + numbers[ind] < len_code and code[k + numbers[ind]] == '#':
                                    k += 1
                                    go_in = True
                                elif code[k + numbers[ind]:].count('#') > sum(contig_st[ind + 1:]):
                                    k += 1
                                    go_in = True
                                else:
                                    go_in = False

                        if try_it:
                            contig_st.append(k)
                            try_it = True
            print('sum_x: ' + str(sum_x))
            sum_a += sum_x

    print(sum_a)
    print(sum_b)


if __name__ == "__main__":
    main()
