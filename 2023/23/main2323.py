
class Graph:
    def __init__(self, f_name: str):
        with open(f_name) as inputtxt:
            lines = inputtxt.readlines()
            self.lines = [x[:-1] for x in lines]

            self.height = len(self.lines)
            self.width = len(self.lines[0])

            lengths = {(self.height - 1, self.width - 2): 0}
            new_vertexes = {(self.height - 1, self.width - 2)}
            self.vertexes = {(self.height - 1, self.width - 2)}

            while len(new_vertexes) > 0:
                new_vertexes = self.iterate(new_vertexes, lengths)
            assert (0, 1) in lengths

        print('part a: ', lengths[(0, 1)])

    def iterate(self, old_vertices: set[tuple[int, int]], lengths: dict[tuple[int, int], int]) -> set[tuple[int, int]]:
        new_vertices = set()
        for old_vertex in old_vertices:
            new_vertices = new_vertices | self.iterate_one_step(old_vertex, lengths)
        return new_vertices

    def iterate_one_step(self, old_vertex: tuple[int, int], lengths: dict[tuple[int, int], int]) -> set[tuple[int, int]]:
        new_vertices = set()
        for neighbour in self.get_neighbours(old_vertex):
            if self.analyze_state(neighbour, lengths, old_vertex):
                new_vertices.add(neighbour)
                lengths[neighbour] = lengths[old_vertex] + 1
        return new_vertices

    @staticmethod
    def get_neighbours(position: tuple[int, int]) -> list[tuple[int, int]]:
        x, y = position
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def reached_from_direction_and_shorter(self, param: tuple[int, int], direction: str, lengths, old_step_length):
        x, y = param
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return True
        if self.lines[x][y] != direction:
            return True
        if param not in lengths:
            return False
        return lengths[param] <= old_step_length

    def reached_from_all_directions_and_argmax(self, param: tuple[int, int], lengths: dict[tuple[int, int], int],
                                               old_step_length: int) -> bool:
        x, y = param
        if not self.reached_from_direction_and_shorter((x - 1, y), '^', lengths, old_step_length):
            return False
        if not self.reached_from_direction_and_shorter((x + 1, y), 'v', lengths, old_step_length):
            return False
        if not self.reached_from_direction_and_shorter((x, y - 1), '<', lengths, old_step_length):
            return False
        if not self.reached_from_direction_and_shorter((x, y + 1), '>', lengths, old_step_length):
            return False
        return True

    def analyze_state(self, param: tuple[int, int], lengths: dict[tuple[int, int], int], old_step: tuple[int, int])\
            -> bool:
        x, y = param
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return False
        if self.lines[x][y] == '#':
            return False
        if (x, y) in lengths:
            return False
        if self.lines[x][y] != '.':
            return True

        old_x, old_y = old_step
        old_step_value = self.lines[old_x][old_y]
        if old_step_value == '.':
            return True
        old_step_length = lengths[old_step]
        if self.reached_from_all_directions_and_argmax(param, lengths, old_step_length):
            return True
        return False



def main():
    Graph('input.txt')


if __name__ == "__main__":
    main()
