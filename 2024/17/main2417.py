def get_val(literal: int, A, B, C):
    if literal < 4:
        return literal
    elif literal == 4:
        return A
    elif literal == 5:
        return B
    elif literal == 6:
        return C
    elif literal == 7:
        return 7
    else:
        raise Exception


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        A = int(lines[0][12:])
        B = int(lines[1][12:])
        C = int(lines[2][12:])

        program_str = lines[4][9:]
        program = program_str.split(',')
        output = []

        ip = 0
        while ip < len(program) - 1:
            opcode = int(program[ip])
            literal = int(program[ip + 1])
            if opcode == 0:
                val = get_val(literal, A, B, C)
                res = A // (2 ** val)
                A = res
            elif opcode == 1:
                res = B ^ literal
                B = res
            elif opcode == 2:
                val = get_val(literal, A, B, C)
                res = val % 8
                B = res
            elif opcode == 3:
                if A != 0:
                    res = get_val(literal, A, B, C)
                    ip = res - 2
            elif opcode == 4:
                res = B ^ C
                B = res
            elif opcode == 5:
                val = get_val(literal, A, B, C)
                res = val % 8
                output.append(res)
            elif opcode == 6:
                val = get_val(literal, A, B, C)
                res = A // (2 ** val)
                B = res
            elif opcode == 7:
                val = get_val(literal, A, B, C)
                res = A // (2 ** val)
                C = res
            else:
                raise Exception
            ip += 2
        print("Part One: ", ','.join([str(x) for x in output]))


def part_two():
    input_str = "2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0"
    program = [int(x) for x in input_str.split(',')]
    A = [0]
    for outp in reversed(program):
        A = [B + 8 * a for B in range(8) for a in A if 3 ^ B ^ (((B + 8 * a) // (2 ** (B ^ 5))) % 8) == outp]
    print("Part Two: ", min(A))


if __name__ == "__main__":
    main()
    part_two()
