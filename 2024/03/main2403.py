import re


def main():
    with open('input.txt') as inputtxt:
        txt = inputtxt.read()
        print('part a: ', func(txt))

        loc = 0
        loc2 = 0

        summ = 0
        while loc != -1 and loc2 != -1:
            loc2 = txt.find('don\'t()', loc)
            summ += func(txt[loc:loc2])
            if loc2 != -1:
                loc = txt.find('do()', loc2)

        print('part b: ', summ)


def func(txt: str):
    pattern = r'mul\((\d+),(\d+)\)'
    results = re.findall(pattern, str(txt))
    summ = 0

    for mo in results:
        summ += int(mo[0]) * int(mo[1])
    return summ


if __name__ == "__main__":
    main()
