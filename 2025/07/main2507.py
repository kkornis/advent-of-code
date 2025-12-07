from collections import Counter


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        sum_a = 0
        state = {lines[0].index('S'): 1}

        for i in range(1, len(lines)):
            new_states = Counter()
            for beam in state:
                if lines[i][beam] == '.':
                    new_states[beam] += state[beam]
                else:
                    assert lines[i][beam] == '^'
                    sum_a += 1
                    if beam - 1 >= 0:
                        new_states[beam - 1] += state[beam]
                    if beam + 1 < len(lines[0]) - 1:
                        new_states[beam + 1] += state[beam]
            state = new_states

        print('Part One: ', sum_a)
        print('Part Two: ', sum(state.values()))


if __name__ == "__main__":
    main()
