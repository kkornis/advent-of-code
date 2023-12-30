
def find_special(line: str, is_backward: bool, digits: dict) -> str:
    len_line = len(line)
    for i in range(len_line):
        for dig_str, dig_int in digits.items():
            if is_backward:
                if line[:-i].endswith(dig_str):
                    return str(dig_int)
            else:
                if line[i:].startswith(dig_str):
                    return str(dig_int)
    raise IndexError


def calculate_with_digits(lines, digits):
    sum_scores = 0
    for i, line in enumerate(lines):
        code = int(find_special(line, False, digits) + find_special(line, True, digits))
        sum_scores += code
    return sum_scores


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        print('part a:', calculate_with_digits(lines, digits))
        digits.update({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                       'nine': 9})
        print('part b:', calculate_with_digits(lines, digits))


if __name__ == "__main__":
    main()
