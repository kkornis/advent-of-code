

def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        mmap = {}

        for line in lines[2:]:
            mmap[line[:3]] = (line[7:10], line[12:15])

        startlist = [x for x in mmap.keys() if x.endswith('A')]
        uniq = ['CKF', 'BMB', 'PSJ', 'VDN', 'NBB', 'FFB']

        map_to_uniq = {x: y for x, y in zip(startlist, uniq)}

        i = 0
        good = False
        state = 'AAA'

        for state in startlist:
            nzs = 0
            i = 0
            good = False
            origstat = state
            visited = set()
            visited.add(state)
            while not good:
                for j, char in enumerate(lines[0][:-1]):
                    if not good:
                        if char == 'R':
                            state = mmap[state][1]
                            i = i + 1
                        if char == 'L':
                            state = mmap[state][0]
                            i = i + 1
                        if state.endswith('Z'):
                            # print(state)
                            print('i: ' + str(i))
                            # print(char)
                            nzs += 1
                if i > 100000:
                    good = True
                    # print(state)
                    # print(nzs)
                else:
                    visited.add(state)
            print(i)


if __name__ == "__main__":
    main()
