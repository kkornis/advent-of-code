from collections import Counter


def main(start):
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        gr = {}

        count_all_paths = Counter()
        count_f1 = Counter()
        count_f2 = Counter()
        count_f12 = Counter()
        count_f21 = Counter()
        for line in lines:
            ind1 = line.find(':')
            targets = line[ind1 + 2:-1].split(' ')
            gr[line[:ind1]] = targets
        gr['out'] = []

        current_subjects = [start]
        processed = set()
        count_all_paths[start] = 1
        count_f1[start] = 0
        count_f2[start] = 0
        count_f12[start] = 0
        count_f21[start] = 0

        i = 0
        while len(current_subjects) > 0:
            new_subjects = []
            for current_one in current_subjects:
                for k in gr[current_one]:
                    # assert k not in processed or count_all_paths[current_one] == 0
                    count_all_paths[k] += count_all_paths[current_one]
                    count_f1[k] += count_f1[current_one]
                    count_f2[k] += count_f2[current_one]
                    count_f12[k] += count_f12[current_one]
                    count_f21[k] += count_f21[current_one]
                    if k in ['dac']:
                        count_f1[k] = count_all_paths[k]
                        count_f12[k] = count_f2[k]
                    if k in ['fft']:
                        count_f2[k] = count_all_paths[k]
                        count_f21[k] = count_f1[k]
                    if k not in new_subjects:
                        new_subjects.append(k)
                        i += 1
                if current_one != 'out':
                    count_all_paths[current_one] = 0
                    count_f1[current_one] = 0
                    count_f2[current_one] = 0
                    count_f12[current_one] = 0
                    count_f21[current_one] = 0
            processed.update(set(current_subjects))
            current_subjects = new_subjects

        part_one = count_all_paths['out']

        part_two = count_f12['out'] + count_f21['out']
        return part_one, part_two


if __name__ == "__main__":
    print("Part one: ", main("you")[0])
    print("Part two: ", main("svr")[1])
