from collections import Counter


dir_map = {'<': (1, 0), '>': (1, 2), '^': (0, 1), 'v': (1, 1), 'A': (0, 2)}
num_map = {'0': (3, 1), '1': (2, 0), '2': (2, 1), '3': (2, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (0, 0),
           '8': (0, 1), '9': (0, 2), 'A': (3, 2)}


def resolve_numeric_keypad(code):
    star_pos = (3, 2)
    res = Counter()
    for c in code:
        char_pos = num_map[c]

        piece = ''
        if char_pos[0] < star_pos[0]:
            if char_pos[1] < star_pos[1]:
                if char_pos[1] == 0 and star_pos[0] == 3:
                    piece += '^' * (star_pos[0] - char_pos[0])
                    piece += '<' * (star_pos[1] - char_pos[1])
                else:
                    piece += '<' * (star_pos[1] - char_pos[1])
                    piece += '^' * (star_pos[0] - char_pos[0])
            elif char_pos[1] > star_pos[1]:
                piece += '^' * (star_pos[0] - char_pos[0])
                piece += '>' * (char_pos[1] - star_pos[1])
            else:
                piece += '^' * (star_pos[0] - char_pos[0])

        elif char_pos[0] > star_pos[0]:
            if char_pos[1] < star_pos[1]:
                piece += '<' * (star_pos[1] - char_pos[1])
                piece += 'v' * (char_pos[0] - star_pos[0])
            elif char_pos[1] > star_pos[1]:
                if star_pos[1] == 0 and char_pos[0] == 3:
                    piece += '>' * (char_pos[1] - star_pos[1])
                    piece += 'v' * (char_pos[0] - star_pos[0])
                else:
                    piece += 'v' * (char_pos[0] - star_pos[0])
                    piece += '>' * (char_pos[1] - star_pos[1])
            else:
                piece += 'v' * (char_pos[0] - star_pos[0])

        else:
            if char_pos[1] < star_pos[1]:
                piece += '<' * (star_pos[1] - char_pos[1])
            elif char_pos[1] > star_pos[1]:
                piece += '>' * (char_pos[1] - star_pos[1])
            else:
                piece += 'v' * (char_pos[0] - star_pos[0])

        star_pos = char_pos

        piece += 'A'
        res[piece] += 1
    return res


def resolve_directional_keypad(code):
    star_pos = (0, 2)
    res = Counter()
    for c in code:
        char_pos = dir_map[c]

        piece = ''
        if char_pos[0] < star_pos[0]:
            if char_pos[1] < star_pos[1]:
                piece += '<' * (star_pos[1] - char_pos[1])
                piece += '^' * (star_pos[0] - char_pos[0])
            elif char_pos[1] > star_pos[1]:
                if char_pos[0] == 0 and star_pos[1] == 0:
                    piece += '>' * (char_pos[1] - star_pos[1])
                    piece += '^' * (star_pos[0] - char_pos[0])
                else:
                    piece += '^' * (star_pos[0] - char_pos[0])
                    piece += '>' * (char_pos[1] - star_pos[1])
            else:
                piece += '^' * (star_pos[0] - char_pos[0])

        elif char_pos[0] > star_pos[0]:
            if char_pos[1] < star_pos[1]:
                if char_pos[1] == 0 and star_pos[0] == 0:
                    piece += 'v' * (char_pos[0] - star_pos[0])
                    piece += '<' * (star_pos[1] - char_pos[1])
                else:
                    piece += '<' * (star_pos[1] - char_pos[1])
                    piece += 'v' * (char_pos[0] - star_pos[0])
            elif char_pos[1] > star_pos[1]:
                piece += 'v' * (char_pos[0] - star_pos[0])
                piece += '>' * (char_pos[1] - star_pos[1])
            else:
                piece += 'v' * (char_pos[0] - star_pos[0])

        else:
            if char_pos[1] < star_pos[1]:
                piece += '<' * (star_pos[1] - char_pos[1])
            elif char_pos[1] > star_pos[1]:
                piece += '>' * (char_pos[1] - star_pos[1])
            else:
                piece += 'v' * (char_pos[0] - star_pos[0])

        star_pos = char_pos

        piece += 'A'
        res[piece] += 1
    return res


def solve(n_mach):
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        sum_a = 0

        for line_dirty in lines:
            line = line_dirty.strip()
            state = resolve_numeric_keypad(line)
            for k in range(n_mach):
                state_new = Counter()
                for world, num in state.items():
                    state_new += Counter({key: val * num for key, val in resolve_directional_keypad(world).items()})
                state = state_new

            sum_a += sum([len(x) * y for x, y in state.items()]) * int(line[:-1])
        return sum_a


if __name__ == "__main__":
    print('Part One: ', solve(2))
    print('Part Two: ', solve(25))
