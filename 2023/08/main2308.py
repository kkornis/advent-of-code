
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a - int(a / b) * b)


def main(part_b: bool):
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        mmap = {}

        instructions = lines[0][:-1]

        for line in lines[2:]:
            mmap[line[:3]] = (line[7:10], line[12:15])

        start_list = ['AAA']
        if part_b:
            start_list = [x for x in mmap.keys() if x.endswith('A')]

        periods = {}

        for state in start_list:
            i = 0
            good = False
            orig_stat = state
            while not good:
                for j, char in enumerate(instructions):
                    if not good:
                        if char == 'R':
                            state = mmap[state][1]
                            i = i + 1
                        if char == 'L':
                            state = mmap[state][0]
                            i = i + 1
                        if state.endswith('Z'):
                            assert j == len(instructions) - 1
                            periods[orig_stat] = i
                            good = True

        res = 1
        for period in periods.values():
            res = res * int(period / gcd(res, period))

        return res


if __name__ == "__main__":
    print('part a:', main(False))
    print('part b:', main(True))
