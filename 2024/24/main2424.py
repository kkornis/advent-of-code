def construct(mem, char):
    i = 0
    key = char + str(i).zfill(2)
    res_int = 0
    while key in mem:
        if mem[key]:
            res_int += 2 ** i
        i += 1
        key = char + str(i).zfill(2)
    return res_int


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

        z_res = construct(mem, 'z')
        print('Part One: ', z_res)

        x_res = construct(mem, 'x')
        y_res = construct(mem, 'y')

        print(abs(x_res + y_res - z_res))


if __name__ == "__main__":
    main()
