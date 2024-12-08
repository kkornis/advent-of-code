def solve(is_b: bool):
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        sum_a = 0
        for line in lines:
            result_s, numbers_s = line.split(': ')
            result = int(result_s)
            numbers = [int(number) for number in numbers_s.split(' ')]
            pres = {numbers[0]}
            for i in range(1, len(numbers)):
                pres_new = set()
                for pre in pres:
                    pres_new.add(pre + numbers[i])
                    pres_new.add(pre * numbers[i])
                    if is_b:
                        pres_new.add(int(str(pre) + str(numbers[i])))
                pres = pres_new
            if result in pres:
                sum_a += result
        return sum_a


def main():
    print('part a: ', solve(False))
    print('part b: ', solve(True))


if __name__ == "__main__":
    main()
