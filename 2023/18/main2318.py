
def process_color(color):
    pass

def main():
    part_b = False
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        width = len(lines[0])
        height = len(lines)
        state_x = 0
        state_y = 0
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        for line in lines:
            direction, amount_str, color = line.split()
            amount = int(amount_str)

            if part_b:
                direction, amount_str = process_color(color)

            if direction == 'U':
                state_x -= amount
            elif direction == 'D':
                state_x += amount
            elif direction == 'L':
                state_y -= amount
            elif direction == 'R':
                state_y += amount
            else:
                raise ValueError
            if state_x < min_x:
                min_x = state_x
            if state_x > max_x:
                max_x = state_x
            if state_y < min_y:
                min_y = state_y
            if state_y > max_y:
                max_y = state_y
        width = max_y - min_y + 1
        height = max_x - min_x + 1
        state_x = -min_x
        state_y = -min_y
        field = [['.' for i in range(width)] for _ in range(height)]

        list_lines = []
        field[state_x][state_y] = '#'
        for k, line in enumerate(lines):
            direction, amount_str, color = line.split()
            amount = int(amount_str)
            if direction == 'U':
                state_x -= amount
                for i in range(amount):
                    field[state_x + i][state_y] = '#'
            elif direction == 'D':
                state_x += amount
                for i in range(amount):
                    field[state_x - i][state_y] = '#'
            elif direction == 'L':
                state_y -= amount
                for i in range(amount):
                    field[state_x][state_y + i] = '#'
            elif direction == 'R':
                state_y += amount
                for i in range(amount):
                    field[state_x][state_y - i] = '#'
            else:
                raise ValueError
            list_lines.append((direction, amount, state_x, state_y, k))

    sum_a = 0
    for i in range(height):
        sum_loc = 0
        is_in = False
        should_enact = True
        for j in range(width):
            if field[i][j] == '.':
                if is_in:
                    sum_loc += 1
            else:
                sum_loc += 1
                if (j == 0 or field[i][j - 1] == '.') and (j == width - 1 or field[i][j + 1] == '.'):
                    is_in = not is_in
                else:
                    concrete_line_spec = None
                    for line_spec in list_lines:
                        if line_spec[2] == i and (line_spec[0] == 'R' or line_spec[0] == 'L'):
                            if line_spec[0] == 'R':
                                if line_spec[3] - line_spec[1] <= j <= line_spec[3]:
                                    assert concrete_line_spec is None
                                    concrete_line_spec = line_spec
                            if line_spec[0] == 'L':
                                if line_spec[3] <= j <= line_spec[3] + line_spec[1]:
                                    assert concrete_line_spec is None
                                    concrete_line_spec = line_spec

                    if concrete_line_spec is None:
                        is_in = not is_in
                    else:
                        if concrete_line_spec[3] == j:
                            ind = concrete_line_spec[4]
                            prev_ind = (ind - 1 if ind > 0 else len(list_lines) - 1)
                            next_ind = (ind + 1 if ind < len(list_lines) - 1 else 0)
                            if list_lines[prev_ind][0] == list_lines[next_ind][0]:
                                is_in = not is_in

        sum_a += sum_loc
        assert not is_in
    print(sum_a)


if __name__ == "__main__":
    main()
