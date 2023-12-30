
class Card:
    def __init__(self, inp: str, converter: {}):
        self.inp = inp
        converted = [converter[x] for x in inp]
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
            max_data = self.data[i][0]
            tmp = [(max_data if x == 1 else x) for x in self.converted]
            tuples = [(y, tmp.count(y)) for y in tmp]
            self.data = sorted(tuples, key=lambda a: a[1] * 100 + a[0], reverse=True)

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
        return False


def main(converter: dict):
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        cards = {}

        for i, line in enumerate(lines):
            num = int(line[6:])
            cards[Card(line[:5], converter)] = num

        mykeys = list(cards.keys())
        mykeys.sort()
        for i, key in enumerate(mykeys):
            if i != 0:
                assert prev_key < key
            prev_key = key
        sum_a = sum([(i + 1) * cards[key] for i, key in enumerate(mykeys)])
        return sum_a


if __name__ == "__main__":
    card_ids = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
                'A': 14}
    print('part a:', main(card_ids))
    card_ids['J'] = 1
    print('part b:', main(card_ids))
