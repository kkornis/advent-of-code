
class Graph:
    def __init__(self, f_name: str):
        self.vertexes: dict[tuple[int, int], dict[tuple[int, int], int]]
        with open(f_name) as inputtxt:
            lines = inputtxt.readlines()
            self.lines = [x[:-1] for x in lines]

            self.height = len(self.lines)
            self.width = len(self.lines[0])

            lengths = {(self.height - 1, self.width - 2): 0}
            new_vertexes = {(self.height - 1, self.width - 2)}
            self.vertexes = {(self.height - 1, self.width - 2): {}}

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
            if self.isvalid(neighbour) and not self.lines[neighbour[0]][neighbour[1]] == '#':
                if self.analyze_state(neighbour, lengths, old_vertex):
                    new_vertices.add(neighbour)
                    lengths[neighbour] = lengths[old_vertex] + 1
                if neighbour not in self.vertexes:
                    self.set_up_new_vertex(neighbour)
                else:
                    if old_vertex not in self.vertexes[neighbour]:
                        self.vertexes[neighbour][old_vertex] = 1
                    if neighbour not in self.vertexes[old_vertex]:
                        self.vertexes[old_vertex][neighbour] = 1
        return new_vertices

    @staticmethod
    def get_neighbours(position: tuple[int, int]) -> list[tuple[int, int]]:
        x, y = position
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    def isvalid(self, position: tuple[int, int]) -> bool:
        x, y = position
        return 0 <= x < self.height and 0 <= y < self.width

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

    def set_up_new_vertex(self, position: tuple[int, int]) -> None:
        self.vertexes[position] = {}
        for neighbour in self.get_neighbours(position):
            if neighbour in self.vertexes:
                if position not in self.vertexes[neighbour]:
                    self.vertexes[neighbour][position] = 1
                if neighbour not in self.vertexes[position]:
                    self.vertexes[position][neighbour] = 1

    def get_longest_route_length(self, vertex1: tuple[int, int], vertex2: tuple[int, int]) -> int:
        while len(self.vertexes) > 2:
            vertex = self.get_vertex_not_eq(vertex1, vertex2)
            if vertex is None:
                break
            self.destroy(vertex)
        return self.find_l_w((133, 131), [vertex1]) + self.vertexes[(140, 139)][(133, 131)]

    def get_vertex_not_eq(self, vertex1: tuple[int, int], vertex2: tuple[int, int]) -> tuple[int, int]:
        for key in self.vertexes.keys():
            if key != vertex1 and key != vertex2:
                if len(self.vertexes[key]) <= 2:
                    return key
        return None

    def destroy(self, vertex: tuple[int, int]) -> None:
        for neighbor1, len1 in self.vertexes[vertex].items():
            for neighbor2, len2 in self.vertexes[vertex].items():
                if neighbor1 != neighbor2:
                    if neighbor2 not in self.vertexes[neighbor1] or len1 + len2 > self.vertexes[neighbor1][neighbor2]:
                        self.vertexes[neighbor1][neighbor2] = len1 + len2
                        self.vertexes[neighbor2][neighbor1] = len1 + len2

        for neighbor1 in self.vertexes[vertex]:
            del self.vertexes[neighbor1][vertex]

        del self.vertexes[vertex]

    def find_l_w(self, destin, path):
        if path[-1] == destin:
            return 0
        max_len = -1
        for neighbour, dist in self.vertexes[path[-1]].items():
            if neighbour not in path:
                len_from_neighbour = self.find_l_w(destin, path + [neighbour])
                if len_from_neighbour > -1 and len_from_neighbour + dist > max_len:
                    max_len = len_from_neighbour + dist
        return max_len


def main():
    graph = Graph('input.txt')
    print('part b:', graph.get_longest_route_length((0, 1), (graph.height - 1, graph.width - 2)))


if __name__ == "__main__":
    main()
