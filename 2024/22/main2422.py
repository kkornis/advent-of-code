from collections import Counter


def nex_secret(secret):
    secret = secret ^ (secret * 64)
    secret = secret % 16777216

    secret = secret ^ (secret // 32)
    secret = secret % 16777216

    secret = secret ^ (secret * 2048)
    secret = secret % 16777216
    return secret


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = Counter()
        for line_dirty in lines:
            rewards = {}
            secret = int(line_dirty.strip())
            p1 = p2 = p3 = p4 = None
            for i in range(2000):
                secret = nex_secret(secret)
                p0 = p1
                p1 = p2
                p2 = p3
                p3 = p4
                p4 = secret % 10
                if i > 3:
                    key = (p1 - p0, p2 - p1, p3 - p2, p4 - p3)
                    if key not in rewards:
                        rewards[key] = p4

            sum_b += Counter(rewards)
            sum_a += secret
        print('Part One: ', sum_a)
        print('Part Two: ', max(sum_b.values()))


if __name__ == "__main__":
    main()
