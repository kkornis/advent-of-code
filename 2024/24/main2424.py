def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        empty_line_ind = 90
        mem = {}
        for line in lines[:empty_line_ind]:
            mem_ind, value = line.strip().split(': ')
            mem[mem_ind] = bool(int(value))

        rel_keys = ['z0' + str(i) for i in range(10)] + ['z' + str(i) for i in range(10, 46)]
        while not all([key in mem for key in rel_keys]):
            for line in lines[empty_line_ind + 1:]:
                inp, output = line.strip().split(' -> ')
                if 'AND' in inp:
                    first, second = inp.split(' AND ')
                    if first in mem and second in mem:
                        mem[output] = mem[first] and mem[second]
                elif 'XOR' in inp:
                    first, second = inp.split(' XOR ')
                    if first in mem and second in mem:
                        mem[output] = mem[first] ^ mem[second]
                elif 'OR' in inp:
                    first, second = inp.split(' OR ')
                    if first in mem and second in mem:
                        mem[output] = mem[first] or mem[second]
                else:
                    raise Exception

        res = 0
        for i in range(10):
            if mem['z0' + str(i)]:
                res += 2 ** i
        for i in range(10, 46):
            if mem['z' + str(i)]:
                res += 2 ** i

        print('Part One: ', res)


if __name__ == "__main__":
    main()
