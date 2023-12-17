def is_place(subject: tuple[int, int, int]) -> bool:
    return 0 <= subject[1] < 110 and 0 <= subject[2] < 110


def determine_new_directions(direction: int, param: str) -> list[int]:
    if param == '.':
        return [direction]
    elif param == '\\':
        if direction == 0:
            return [2]
        elif direction == 1:
            return [3]
        elif direction == 2:
            return [0]
        elif direction == 3:
            return [1]
        else:
            raise ValueError
    elif param == '/':
        if direction == 0:
            return [3]
        elif direction == 1:
            return [2]
        elif direction == 2:
            return [1]
        elif direction == 3:
            return [0]
        else:
            raise ValueError
    elif param == '-':
        if direction == 0:
            return [0]
        elif direction == 1:
            return [1]
        elif direction == 2:
            return [0, 1]
        elif direction == 3:
            return [0, 1]
        else:
            raise ValueError
    elif param == '|':
        if direction == 0:
            return [2, 3]
        elif direction == 1:
            return [2, 3]
        elif direction == 2:
            return [2]
        elif direction == 3:
            return [3]
        else:
            raise ValueError
    else:
        raise ValueError


def apply_beam_raw(subject: tuple[int, int, int], param: str) -> list[tuple[int, int, int]]:
    new_directions = determine_new_directions(subject[0], param)
    new_subjects = []
    for new_direction in new_directions:
        if new_direction == 0:
            new_subjects.append((new_direction, subject[1], subject[2] + 1))
        elif new_direction == 1:
            new_subjects.append((new_direction, subject[1], subject[2] - 1))
        elif new_direction == 2:
            new_subjects.append((new_direction, subject[1] + 1, subject[2]))
        elif new_direction == 3:
            new_subjects.append((new_direction, subject[1] - 1, subject[2]))
    return new_subjects


def apply_beam(subject: tuple[int, int, int], param: str) -> list[tuple[int, int, int]]:
    return [x for x in apply_beam_raw(subject, param) if is_place(x)]


def main():
    with open('input.txt') as inputtxt:

        sum_a = 0
        sum_b = 0

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        width = len(lines[0])
        height = len(lines)

        l_max = -1
        for i in range(110):
            print(i, l_max)
            res_0 = second_part((0, i, 0), width, height, lines)
            res_1 = second_part((1, i, 109), width, height, lines)
            res_2 = second_part((2, 0, i), width, height, lines)
            res_3 = second_part((3, 109, i), width, height, lines)

            l2_max = max(res_0, res_1, res_2, res_3)
            if l2_max > l_max:
                l_max = l2_max
        print(l_max)


def second_part(first_subject: tuple[int, int, int], width, height, lines) -> int:
    final_data = [[False] * width for i in range(height)]

    unhandled = [first_subject]
    start = 0
    end = 1

    f = 0
    while end - start > 0:
        f += 1
        # print(f, start, end)
        subject = unhandled[start]
        new_subjects = apply_beam(subject, lines[subject[1]][subject[2]])
        new_subjects = [x for x in new_subjects if x not in unhandled]
        unhandled.extend(new_subjects)
        end += len(new_subjects)
        start += 1

    for subject in unhandled:
        final_data[subject[1]][subject[2]] = True

    return sum([sum(x) for x in final_data])


if __name__ == "__main__":
    main()
