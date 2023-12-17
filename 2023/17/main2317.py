
def main():
    with open('input.txt') as inputtxt:

        sum_a = 0
        sum_b = 0

        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        width = len(lines[0])
        height = len(lines)

        # 0: horizontal, 1: vertical movement | row ind | col ind

        reached: dict[tuple[int, int, int], int] = {}
        reached[(0, height - 1, width - 1)] = 0
        reached[(1, height - 1, width - 1)] = 0
        is_new = True
        t = 0
        while is_new and ((0, 0, 0) not in reached or (1, 0, 0) not in reached):
            t += 1
            if t % 20 == 0:
                print(t, len(reached))
            is_new = False
            # candidates: dict[tuple[int, int, int], int] = {}
            candidates = []

            for vertex, val in reached.items():
                s0p = int(lines[vertex[1]][vertex[2]])
                s0n = int(lines[vertex[1]][vertex[2]])
                if vertex[0] == 0:
                    for i in range(1, 4):
                        if vertex[1] + i < height:
                            candidates.append((1, vertex[1] + i, vertex[2], val + s0p))
                            s0p += int(lines[vertex[1] + i][vertex[2]])
                        if vertex[1] - i >= 0:
                            candidates.append((1, vertex[1] - i, vertex[2], val + s0n))
                            s0n += int(lines[vertex[1] - i][vertex[2]])
                elif vertex[0] == 1:
                    for i in range(1, 4):
                        if vertex[2] + i < width:
                            candidates.append((0, vertex[1], vertex[2] + i, val + s0p))
                            s0p += int(lines[vertex[1]][vertex[2] + i])
                        if vertex[2] - i >= 0:
                            candidates.append((0, vertex[1], vertex[2] - i, val + s0n))
                            s0n += int(lines[vertex[1]][vertex[2] - i])

            filtered_candidates: dict[tuple[int, int, int], int] = {}
            for candidate in candidates:
                key = (candidate[0], candidate[1], candidate[2])
                if key in reached:
                    assert reached[key] <= candidate[3]
                elif key in filtered_candidates:
                    if filtered_candidates[key] > candidate[3]:
                        filtered_candidates[key] = candidate[3]
                else:
                    filtered_candidates[key] = candidate[3]

            if len(filtered_candidates) == 0:
                assert len(reached) == 2 * height * width
            else:
                minn = 10 ** 10
                key = None
                for cand, value in filtered_candidates.items():
                    if value < minn:
                        minn = value
                        key = (cand[0], cand[1], cand[2])
                reached[key] = minn
                is_new = True
        print(reached[(0, 0, 0)])
        print(reached[(1, 0, 0)])
        print(min(reached[(0, 0, 0)], reached[(1, 0, 0)]))


if __name__ == "__main__":
    main()
