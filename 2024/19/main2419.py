def count_constructions(towel: str, constituents: list[str]) -> int:
    n_constructions = [1]
    for i in range(len(towel)):
        n_constructions.append(0)
        for constituent in constituents:
            if towel[-i-1:].startswith(constituent):
                n_constructions[-1] += n_constructions[-len(constituent)-1]
    return n_constructions[-1]


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        constituents = lines[0][:-1].split(', ')

        n_constructions = [count_constructions(towel[:-1], constituents) for towel in lines[2:]]
        print('Part One: ', sum([x > 0 for x in n_constructions]))
        print('Part Two: ', sum(n_constructions))


if __name__ == "__main__":
    main()
