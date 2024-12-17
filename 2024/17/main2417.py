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


def part_one(progr, A, B, C):
        output = []

        ip = 0
        while ip < len(progr) - 1:
            opcode = progr[ip]
            literal = progr[ip + 1]
            combo_operand = get_val(literal, A, B, C)
            if opcode == 0:
                res = A // (2 ** combo_operand)
                A = res
            elif opcode == 1:
                B = B ^ literal
            elif opcode == 2:
                B = combo_operand % 8
            elif opcode == 3:
                if A != 0:
                    ip = combo_operand - 2
            elif opcode == 4:
                B = B ^ C
            elif opcode == 5:
                output.append(combo_operand % 8)
            elif opcode == 6:
                B = A // (2 ** combo_operand)
            elif opcode == 7:
                C = A // (2 ** combo_operand)
            else:
                raise Exception
            ip += 2
        print("Part One: ", ','.join([str(x) for x in output]))


def part_two(progr):
    A = [0]
    for outp in reversed(progr):
        A = [B + 8 * a for B in range(8) for a in A if 3 ^ B ^ (B + 8 * a) // 2 ** (B ^ 5) % 8 == outp]
    print("Part Two: ", min(A))


if __name__ == "__main__":
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        A = int(lines[0][12:])
        B = int(lines[1][12:])
        C = int(lines[2][12:])

        program_str = lines[4][9:]
        program = [int(x) for x in program_str.split(',')]

        part_one(program, A, B, C)
        part_two(program)
