digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
str_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
digits.update(str_digits)


def find_sp_forward(line: str) -> str:
    len_line = len(line)
    for i in range(len_line):
        for dig_str, dig_int in digits.items():
            if line[i:].startswith(dig_str):
                return str(dig_int)
    raise IndexError


def find_sp_backward(line: str) -> str:
    len_line = len(line)
    for i in range(len_line):
        for dig_str, dig_int in digits.items():
            if line[:-i].endswith(dig_str):
                return str(dig_int)
    raise IndexError


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        sum_scores = 0
        for i, line in enumerate(lines):
            code = int(find_sp_forward(line) + find_sp_backward(line))
            sum_scores += code
        print(sum_scores)


if __name__ == "__main__":
    main()
