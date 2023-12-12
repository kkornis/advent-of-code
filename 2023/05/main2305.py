def proc(lines, start, end):
    return [[int(x) for x in line[:-1].split()] for line in lines[start: end]]


def apply_old(num, x_map):
    for line in x_map:
        if line[1] <= num < line[1] + line[2]:
            return num + line[0] - line[1]
    return num


class Range:
    def __init__(self, start: int, length: int):
        self.start: int = start
        self.length: int = length


class Mapping:
    def __init__(self, sections: list[tuple[Range, int]]):
        self.sections: list[tuple[Range, int]] = sections

    def apply_range(self, x_range: Range) -> list[Range]:
        for my_range, shift in self.sections:
            if x_range.start < my_range.start:
                if x_range.start + x_range.length <= my_range.start:
                    pass
                else:
                    return self.apply_l_ranges([Range(x_range.start, my_range.start - x_range.start),
                                                Range(my_range.start, x_range.length - my_range.start + x_range.start)])
            elif x_range.start >= my_range.start + my_range.length:
                pass
            elif my_range.start <= x_range.start < my_range.start + my_range.length:
                if x_range.start + x_range.length <= my_range.start + my_range.length:
                    return [Range(x_range.start + shift, x_range.length)]
                else:
                    first_l_r = self.apply_range(Range(x_range.start, my_range.start + my_range.length - x_range.start))
                    second_l_r = self.apply_range(Range(my_range.start + my_range.length,
                                                  x_range.start + x_range.length - my_range.start - my_range.length))
                    return first_l_r + second_l_r
            else:
                raise ValueError
        return [x_range]

    def apply_l_ranges(self, l_ranges: list[Range]) -> list[Range]:
        ret = []
        for x_range in l_ranges:
            ret.extend(self.apply_range(x_range))
        return ret


def proc_new(lines, start, end) -> Mapping:
    sections: list[tuple[Range, int]] = []
    for line in lines[start: end]:
        x, y, z = line[:-1].split()
        sections.append((Range(int(y), int(z)), int(x) - int(y)))
    return Mapping(sections)


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        seeds = [int(x) for x in lines[0][7:].split()]
        seeds_new = []
        for i in range(int(len(seeds) / 2)):
            seed_start = seeds[2 * i]
            seed_length = seeds[2 * i + 1]
            seeds_new.append(Range(seed_start, seed_length))
        seeds = seeds_new

        seed_to_soil = proc_new(lines, 3, 32)
        soil_to_fert = proc_new(lines, 34, 53)
        fert_to_water = proc_new(lines, 55, 97)
        water_to_light = proc_new(lines, 99, 117)
        light_to_temp = proc_new(lines, 119, 132)
        temp_to_hum = proc_new(lines, 134, 144)
        hum_to_loc = proc_new(lines, 146, 190)

        seeds1 = seed_to_soil.apply_l_ranges(seeds)
        seeds2 = soil_to_fert.apply_l_ranges(seeds1)
        seeds3 = fert_to_water.apply_l_ranges(seeds2)
        seeds4 = water_to_light.apply_l_ranges(seeds3)
        seeds5 = light_to_temp.apply_l_ranges(seeds4)
        seeds6 = temp_to_hum.apply_l_ranges(seeds5)
        seeds7 = hum_to_loc.apply_l_ranges(seeds6)
        print(min([rang.start for rang in seeds7]))


if __name__ == "__main__":
    main()
