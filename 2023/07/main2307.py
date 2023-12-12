import re


def convert(c) -> int:
    if c == '2':
        return 2
    elif c == '3':
        return 3
    elif c == '4':
        return 4
    elif c == '5':
        return 5
    elif c == '6':
        return 6
    elif c == '7':
        return 7
    elif c == '8':
        return 8
    elif c == '9':
        return 9
    elif c == 'T':
        return 10
    elif c == 'J':
        return 1
    elif c == 'Q':
        return 12
    elif c == 'K':
        return 13
    elif c == 'A':
        return 14


class Card:
    def __init__(self, inp: str):
        self.inp = inp
        converted = [convert(x) for x in inp]
        self.converted = converted
        tuples = [(y, converted.count(y)) for y in converted]
        njs = converted.count(1)
        if njs == 5:
            self.data = [(14, 5), (14, 5), (14, 5), (14, 5), (14, 5)]
        else:
            self.data = sorted(tuples, key=lambda a: a[1] * 100 + a[0], reverse=True)
            i = 0
            while self.data[i][0] == 1:
                i += 1
            maxx = self.data[i][0]
            tmp = [(maxx if x == 1 else x) for x in self.converted]
            tuples = [(y, tmp.count(y)) for y in tmp]
            self.data = sorted(tuples, key=lambda a: a[1] * 100 + a[0], reverse=True)

        # print(self.data)

    def __lt__(self, other):
        a = self.data
        b = other.data
        for i in range(5):
            if a[i][1] < b[i][1]:
                return True
            if a[i][1] > b[i][1]:
                return False
        for i in range(5):
            if self.converted[i] < other.converted[i]:
                return True
            if self.converted[i] > other.converted[i]:
                return False

        # for i in range(5):
        #     if a[i][0] < b[i][0]:
        #         return True
        #     if a[i][0] > b[i][0]:
        #         return False
        return False


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        sum_a = 0
        sum_b = 0

        cards = {}

        num_lines = len(lines)
        for i, line in enumerate(lines):
            num = int(line[6:])
            cards[Card(line[:5])] = num
            print(num)

        # xcv = list(cards.keys())[0:5]
        # print(xcv[0] < xcv[1])


        mykeys = list(cards.keys())
        mykeys.sort()
        for i, key in enumerate(mykeys):
            if i != 0:
                assert prevkey < key
            prevkey = key
        sorted_dict = {i: cards[i] for i in mykeys}
        sum_a = sum([(i + 1) * cards[key] for i, key in enumerate(mykeys)])

        for i, key in enumerate(mykeys):
            print(key.data)
        print(sum_a)
        print(sum_b)


if __name__ == "__main__":
    main()

#253702560
#253638586