from collections import Counter


def enrich_simple(key: str):
    prev = key[0]
    rep = 1
    new = ""
    for l in key[1:]:
        if l == prev:
            rep += 1
        else:
            new = new + str(rep) + prev
            rep = 1
            prev = l
    new = new + str(rep) + prev
    return new


def enrich(compressed_inp: Counter) -> Counter:
    new_compressed_inp = Counter()
    for key, value in compressed_inp.items():
        enricher_one = enrich_simple(key)
        new_compressed_inp[enricher_one] += value
    return new_compressed_inp


def main():
    my_input = "1321131112"

    for i in range(40):
        my_input = enrich_simple(my_input)

    print("Part one:", len(my_input))

    sec_size = 50000
    prev_subsection = None
    len_so_far = 0
    max_allowed_error = 150
    start_overlap = 100
    est_overlap = int(start_overlap * pow(1.303577269034, 10))
    for i in range(10):
        print("iterations: ", i)
        inp = my_input

        st_i = i * sec_size
        end_i = (i + 1) * sec_size
        st_i -= start_overlap // 2
        end_i += start_overlap // 2
        st_i = max(st_i, 0)
        end_i = min(end_i, 492982)

        subsection = inp[st_i: end_i]
        for j in range(10):
            subsection = enrich_simple(subsection)
        if prev_subsection is None:
            len_so_far = len(subsection)
        else:
            overlap = None
            for cand_overlap in range(est_overlap - 800, est_overlap + 1000):
                prev_end_section = prev_subsection[-cand_overlap + max_allowed_error:-max_allowed_error]
                curr_begin_section = subsection[max_allowed_error:cand_overlap - max_allowed_error]
                assert cand_overlap - 2 * max_allowed_error > 100
                if prev_end_section == curr_begin_section:
                    assert overlap is None
                    overlap = cand_overlap
            assert overlap is not None
            len_so_far += len(subsection) - overlap
        prev_subsection = subsection

    print("Part one:", len(my_input))
    print("Part two:", len_so_far)


if __name__ == "__main__":
    main()
