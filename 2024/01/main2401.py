def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        flist = []
        slist = []

        for i, line in enumerate(lines):
            x = line.split(' ')
            flist.append(int(x[0]))
            slist.append(int(x[-1]))

        sum_b = 0
        flist.sort()
        slist.sort()
        for x, y in zip(flist, slist):
            sum_b += abs(x - y)
        print('part a: ', sum_b)

        score = 0
        for x in flist:
            score += x * slist.count(x)
        print('part b: ', score)


if __name__ == "__main__":
    main()
