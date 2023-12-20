conv_unit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


def conv_dec(amount_hex: str) -> int:
    res = 0
    for i in range(len(amount_hex)):
        res *= 16
        res += conv_unit[amount_hex[i]]
    return res


color_dir_map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def process_color(color):
    direction = color_dir_map[color[-1]]

    amount_hex = color[1:-1]
    return direction, conv_dec(amount_hex)


def main(part_b: bool):
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]

        state_x = 0
        state_y = 0

        sum_b = 0
        sum_amm = 0

        for line in lines:
            direction, amount, color = line.split()

            if part_b:
                direction, amount = process_color(color[1: -1])
            else:
                amount = int(amount)

            if direction == 'U':
                state_x -= amount
                sum_b -= state_y * amount
            elif direction == 'D':
                state_x += amount
                sum_b += state_y * amount
            elif direction == 'L':
                state_y -= amount
            elif direction == 'R':
                state_y += amount
            else:
                raise ValueError
            sum_amm += amount
        print('part ' + ('b' if part_b else 'a') + ': ', sum_b + int(sum_amm / 2) + 1)


if __name__ == "__main__":
    main(False)
    main(True)
