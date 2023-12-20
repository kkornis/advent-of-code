
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

    def is_in_original_state(self) -> bool:
        raise NotImplementedError


class Broadcaster(Module):
    def __init__(self, name: str, destinations: list[str]):
        super().__init__(name, destinations)

    def receive(self, pulse: bool, from_name: str) -> list[tuple[str, str, bool]]:
        return [(self.name, dest, pulse) for dest in self.destinations]

    def is_in_original_state(self) -> bool:
        return True


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

    def is_in_original_state(self) -> bool:
        return not self.button


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

    def is_in_original_state(self) -> bool:
        return all([(not x) for x in self.connected_inputs.values()])


def iterate(signs, modules):
    result = []
    for from_name, to, pulse in signs:
        if to in modules:
            result.extend(modules[to].receive(pulse, from_name))
    return result


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        modules = {}

        for line in lines:
            my_module = create_module(line)
            modules[my_module.name] = my_module

        for module in modules.values():
            module.set_up(list(modules.values()))

        n_lows_sum = 0
        n_highs_sum = 0
        for j in range(1000):
            signs = [['button', 'broadcaster', False]]
            while len(signs) > 0:
                for sign in signs:
                    if sign[2]:
                        n_highs_sum += 1
                    else:
                        n_lows_sum += 1
                signs = iterate(signs, modules)

        print(n_lows_sum)
        print(n_highs_sum)
        print(n_lows_sum * n_highs_sum)


if __name__ == "__main__":
    main()
