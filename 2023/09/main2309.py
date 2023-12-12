

def main():
    with open('input.txt') as inputtxt:

        lines = inputtxt.readlines()
        sum_a = 0
        sum_b = 0

        for line in lines:
            numbers = line[:-1].split()
            numbers = [int(x) for x in numbers]

            ends = []
            starts = []
            while any([x != 0 for x in numbers]):
                ends.append(numbers[-1])
                starts.append(numbers[0])
                numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

            sum_a += sum(ends)
            sum_b += sum([starts[i] * ((-1) ** i) for i in range(len(starts))])

    print(sum_a)
    print(sum_b)


if __name__ == "__main__":
    main()
