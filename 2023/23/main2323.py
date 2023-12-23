def reached_from_direction_and_shorter(param: tuple[int, int], direction: str, lengths, lines, width, height, old_step_length):
    x, y = param
    if x < 0 or x >= height or y < 0 or y >= width:
        return True
    if lines[x][y] != direction:
        return True
    if param not in lengths:
        return False
    return lengths[param] <= old_step_length


def reached_from_all_directions_and_argmax(param: tuple[int, int], lengths: dict[tuple[int, int], int],
                                           lines: list[str], width: int, height: int, old_step_length: int) -> bool:
    x, y = param
    if not reached_from_direction_and_shorter((x - 1, y), '^', lengths, lines, width, height, old_step_length):
        return False
    if not reached_from_direction_and_shorter((x + 1, y), 'v', lengths, lines, width, height, old_step_length):
        return False
    if not reached_from_direction_and_shorter((x, y - 1), '<', lengths, lines, width, height, old_step_length):
        return False
    if not reached_from_direction_and_shorter((x, y + 1), '>', lengths, lines, width, height, old_step_length):
        return False
    return True


def analyze_state(param: tuple[int, int], lengths: dict[tuple[int, int], int], lines: list[str], width: int,
                  height: int, old_step: tuple[int, int]) -> bool:
    x, y = param
    if x < 0 or x >= height or y < 0 or y >= width:
        return False
    if lines[x][y] == '#':
        return False
    if (x, y) in lengths:
        return False
    if lines[x][y] != '.':
        return True

    old_x, old_y = old_step
    old_step_value = lines[old_x][old_y]
    if old_step_value == '.':
        return True
    old_step_length = lengths[old_step]
    if reached_from_all_directions_and_argmax(param, lengths, lines, width, height, old_step_length):
        return True
    return False


def iterate_one_step(old_step: tuple[int, int], lengths: dict[tuple[int, int], int], lines: list[str], width: int,
                     height: int) -> set[tuple[int, int]]:
    new_steps = set()
    x, y = old_step
    if analyze_state((x - 1, y), lengths, lines, width, height, old_step):
        new_steps.add((x - 1, y))
        lengths[(x - 1, y)] = lengths[(x, y)] + 1
    if analyze_state((x + 1, y), lengths, lines, width, height, old_step):
        new_steps.add((x + 1, y))
        lengths[(x + 1, y)] = lengths[(x, y)] + 1
    if analyze_state((x, y - 1), lengths, lines, width, height, old_step):
        new_steps.add((x, y - 1))
        lengths[(x, y - 1)] = lengths[(x, y)] + 1
    if analyze_state((x, y + 1), lengths, lines, width, height, old_step):
        new_steps.add((x, y + 1))
        lengths[(x, y + 1)] = lengths[(x, y)] + 1
    return new_steps


def iterate(old_steps: set[tuple[int, int]], lengths: dict[tuple[int, int], int], lines: list[str], width: int,
            height: int) -> set[tuple[int, int]]:
    new_steps = set()
    for old_step in old_steps:
        new_steps = new_steps | iterate_one_step(old_step, lengths, lines, width, height)
    return new_steps


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]

        sum_a = 0
        sum_b = 0

        height = len(lines)
        width = len(lines[0])

        lengths = {(height - 1, width - 2): 1}
        new_steps = {(height - 1, width - 2)}
        while (0, 1) not in lengths:
            assert len(new_steps) > 0
            new_steps = iterate(new_steps, lengths, lines, width, height)

        print('part a: ', lengths[(0, 1)] - 1)
        print('part b: ', sum_b)


if __name__ == "__main__":
    main()
