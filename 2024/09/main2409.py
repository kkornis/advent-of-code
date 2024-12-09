# This code is terrible, don't see it!

def main_a():
    with open('input.txt') as inputtxt:
        txt = inputtxt.read()
        le = len(txt)
        print(le)
        print(txt[-3:])

        explen = sum(int(x) for i, x in enumerate(txt) if (i % 2 == 0))

        flist = []
        indforw = 0
        intbackw = le - 2
        leftover = int(txt[intbackw])
        while indforw <= intbackw:
            for i in range(int(txt[indforw])):
                flist.append(indforw // 2)
                if len(flist) == explen:
                    break
            if len(flist) == explen:
                break
            indforw += 1
            space = int(txt[indforw])
            while space > 0:
                if leftover > 0:
                    flist.append(intbackw // 2)
                    if len(flist) == explen:
                        break
                    leftover -= 1
                    space -= 1
                    if leftover == 0:
                        intbackw -= 2
                        leftover = int(txt[intbackw])
            if len(flist) == explen:
                break
            indforw += 1

        sum_a = 0
        for i, x in enumerate(flist):
            sum_a += i * x
        print(sum_a)


def main_b():
    with open('input.txt') as inputtxt:
        txt = inputtxt.read()
        le = len(txt)

        mystr = []
        indxs = []
        for i, ch in enumerate(txt[:-1]):
            if i % 2 == 0:
                assert i // 2 == len(indxs)
                indxs.append((len(mystr), int(ch)))
                for j in range(int(ch)):
                    mystr.append(i//2)
            else:
                for j in range(int(ch)):
                    mystr.append(-1)

        len_indexs = len(indxs)
        for i in range(len_indexs):
            curr_pos_in_mystr, next_len = indxs[len_indexs - i - 1]
            j = 0
            lensf = 0
            while j < curr_pos_in_mystr:
                if mystr[j] == -1:
                    lensf += 1
                    if lensf == next_len:
                        break
                else:
                    lensf = 0
                j += 1
            if j != curr_pos_in_mystr:
                content = len_indexs - i - 1
                for w in range(next_len):
                    mystr[j - w] = content

                for w in range(next_len):
                    assert mystr[curr_pos_in_mystr + w] == content
                    mystr[curr_pos_in_mystr + w] = -1

        sum_x = 0
        for i, ch in enumerate(mystr):
            if ch != -1:
                sum_x += i * ch
        print(sum_x)


def main():
    main_b()


if __name__ == "__main__":
    main()
