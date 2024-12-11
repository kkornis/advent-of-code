import math


def blink(stones: dict[int, int]) -> dict[int, int]:
    new_stones = {}
    for stone, freq in stones.items():
        if stone == 0:
            news = [1]
        elif int(math.log10(stone)) % 2 == 1:
            len_stone = int(math.log10(stone)) + 1
            new_len = len_stone // 2
            news = [stone // (10 ** new_len), stone % (10 ** new_len)]
        else:
            news = [stone * 2024]
        for new_stone in news:
            if new_stone in new_stones:
                new_stones[new_stone] += freq
            else:
                new_stones[new_stone] = freq
    return new_stones


def main():
    with open('input.txt') as inputtxt:
        txt = inputtxt.read()
        stones = {int(x): 1 for x in txt[:-1].split(' ')}

        for i in range(25):
            stones = blink(stones)
        print('Part One: ', sum(stones.values()))

        for i in range(50):
            stones = blink(stones)
        print('Part Two: ', sum(stones.values()))


if __name__ == "__main__":
    main()
