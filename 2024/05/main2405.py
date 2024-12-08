def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        div_line_ind = lines.index("\n")

        rules_x = lines[:div_line_ind]
        updates_x = lines[div_line_ind+1:]

        rules = [[int(y) for y in x.split('|')] for x in rules_x]
        updates = [[int(y) for y in x.split(',')] for x in updates_x]

        for rule in rules:
            assert len(rule) == 2

        summ = 0
        summ_b = 0
        for update in updates:
            correct = True
            for rule in rules:
                if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
                    correct = False
            if correct:
                assert len(update) % 2 == 1
                summ += update[(len(update) - 1) // 2]
            else:
                corrected = []
                while len(update) > 0:
                    candid = None
                    for p_next in update:
                        fit = True
                        for rule in rules:
                            if rule[0] in update and rule[1] == p_next:
                                fit = False
                        if fit:
                            candid = p_next
                            corrected.append(candid)
                            update.pop(update.index(candid))
                            break
                    assert candid is not None, "it is not possible to fix"

                assert len(corrected) % 2 == 1
                summ_b += corrected[(len(corrected) - 1) // 2]

        print('part a: ', summ)
        print('part b: ', summ_b)


if __name__ == "__main__":
    main()
