
def create_module(line: str):
    first_part, second_part = line[:-1].split(' -> ')
    destinations = second_part.split(', ')
    if first_part[0] == '%':
        return FlipFlop(first_part[1:], destinations)
    elif first_part[0] == '&':
        return Conjunction(first_part[1:], destinations)
    elif first_part[0] == 'b':
        return Broadcaster('broadcaster', destinations)
    else:
        raise ValueError


class Module:
    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self.destinations = destinations
        self.button = False

    # high: True, low: False
    def receive(self, pulse: bool, from_name: str) -> list[tuple[str, str, bool]]:
        raise NotImplementedError

    def set_up(self, others: list):
        pass


class Broadcaster(Module):
    def __init__(self, name: str, destinations: list[str]):
        super().__init__(name, destinations)

    def receive(self, pulse: bool, from_name: str) -> list[tuple[str, str, bool]]:
        return [(self.name, dest, pulse) for dest in self.destinations]


class FlipFlop(Module):
    def __init__(self, name: str, destinations: list[str]):
        super().__init__(name, destinations)

    def receive(self, pulse: bool, from_name: str) -> list[tuple[str, str, bool]]:
        if not pulse:
            if self.button:
                self.button = False
                return [(self.name, dest, False) for dest in self.destinations]
            else:
                self.button = True
                return [(self.name, dest, True) for dest in self.destinations]
        else:
            return []


class Conjunction(Module):
    def __init__(self, name: str, destinations: list[str]):
        super().__init__(name, destinations)
        self.connected_inputs = {}

    def set_up(self, others: list):
        for other in others:
            if self.name in other.destinations:
                self.connected_inputs[other.name] = False

    def receive(self, pulse: bool, from_name: str) -> list[tuple[str, str, bool]]:
        self.connected_inputs[from_name] = pulse
        output_pulse = not all(self.connected_inputs.values())
        return [(self.name, dest, output_pulse) for dest in self.destinations]


def gcd(a, b):
    if a == b:
        return a
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(a - int(a / b) * b, b)


def main():
    with open('input.txt') as inputtxt:
        roots = ['bt', 'ml', 'rb', 'gp']
        roots_res = {}
        lines = inputtxt.readlines()
        modules = {}

        for line in lines:
            my_module = create_module(line)
            modules[my_module.name] = my_module

        for module in modules.values():
            module.set_up(list(modules.values()))

        n_lows_sum = 0
        n_highs_sum = 0
        j = 0
        while len(roots_res) < 4:
            signs = [['button', 'broadcaster', False]]
            loc_iter = 0
            while len(signs) > loc_iter:
                from_name, to, pulse = signs[loc_iter]
                for root in roots:
                    if from_name == root and not pulse and root not in roots_res:
                        roots_res[root] = j + 1
                if pulse:
                    n_highs_sum += 1
                else:
                    n_lows_sum += 1
                if to in modules:
                    signs.extend(modules[to].receive(pulse, from_name))
                loc_iter += 1
            j += 1

        print(n_lows_sum * n_highs_sum)
        res_b = 1
        for val in roots_res.values():
            my_gcd = gcd(res_b, val)
            res_b *= int(val / my_gcd)
        print(res_b)


if __name__ == "__main__":
    main()
