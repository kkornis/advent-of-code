def create_tuple(box, ind, int_start, int_end):
    if ind == 0:
        return int_start, int_end, box[2], box[3], box[4], box[5], box[6], box[7]
    elif ind == 2:
        return box[0], box[1], int_start, int_end, box[4], box[5], box[6], box[7]
    elif ind == 4:
        return box[0], box[1], box[2], box[3], int_start, int_end, box[6], box[7]
    elif ind == 6:
        return box[0], box[1], box[2], box[3], box[4], box[5], int_start, int_end


letter_map = {'x': 0, 'm': 2, 'a': 4, 's': 6}


def apply_cond(box: tuple[int, int, int, int, int, int, int, int], unequality: str):
    if box is None:
        return None, None
    ind = letter_map[unequality[0]]
    direction = unequality[1]
    number = int(unequality[2:])
    if direction == '<':
        if number <= box[ind]:
            return box, None
        elif number <= box[ind + 1]:
            return create_tuple(box, ind, number, box[ind + 1]), create_tuple(box, ind, box[ind], number)
        return None, box
    elif direction == '>':
        if number >= box[ind + 1]:
            return box, None
        elif number >= box[ind]:
            return create_tuple(box, ind, box[ind], number + 1), create_tuple(box, ind, number + 1, box[ind + 1])
        return None, box
    else:
        raise ValueError


def step(states: list[tuple[str, tuple[int, int, int, int, int, int, int, int]]],
         workflows: dict[str, tuple[list[str], str]])\
        -> list[tuple[str, tuple[int, int, int, int, int, int, int, int]]]:
    new_states = []
    for state in states:
        if state[0] == 'A' or state[0] == 'R':
            new_states.append(state)
        else:
            box = state[1]
            conditions, unconditional = workflows[state[0]]
            for condition in conditions:
                unequality, destination = condition.split(':')
                box, new_box = apply_cond(box, unequality)
                if new_box is not None:
                    new_states.append((destination, new_box))
            if box is not None:
                new_states.append((unconditional, box))
    return new_states


def main(part_a: bool):
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        is_workflow_part = True
        workflows = {}
        pieces = []

        for line in lines:
            if line == '\n':
                is_workflow_part = False
            elif is_workflow_part:
                wf_name, remaining = line.split('{')
                conditions_str = remaining[:-2].split(',')
                workflows[wf_name] = (conditions_str[:-1], conditions_str[-1])
            else:
                pieces.append([int(x[2:]) for x in line[1:-2].split(',')])

        if part_a:
            states = [('in', (x, x + 1, m, m + 1, a, a + 1, s, s + 1)) for x, m, a, s in pieces]
        else:
            states = [('in', (1, 4001, 1, 4001, 1, 4001, 1, 4001))]
        while not all([(x[0] == 'A' or x[0] == 'R') for x in states]):
            states = step(states, workflows)

        sum_a = 0
        for state in states:
            if state[0] == 'A':
                box = state[1]
                if part_a:
                    sum_a += box[0] + box[2] + box[4] + box[6]
                else:
                    sum_a += (box[1] - box[0]) * (box[3] - box[2]) * (box[5] - box[4]) * (box[7] - box[6])

        return sum_a


if __name__ == "__main__":
    print('part a:', main(True))
    print('part b:', main(False))
