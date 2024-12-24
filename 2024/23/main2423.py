import itertools


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()
        vertices = set()
        edges = set()
        for line in lines:
            edge = line.strip()
            va, vb = edge.split('-')
            vertices.add(va)
            vertices.add(vb)
            edges.add(edge)

        n_t_triangles = 0
        for edge in edges:
            v1, v2 = edge.split('-')
            for vertex in vertices:
                if v1 != vertex and v2 != vertex and ('t' == v1[0] or 't' == v2[0] or 't' == vertex[0]):
                    if ((v1 + '-' + vertex) in edges or (vertex + '-' + v1) in edges) and (
                            (v2 + '-' + vertex) in edges or (vertex + '-' + v2) in edges):
                        n_t_triangles += 1
        print('Part One: ', n_t_triangles // 3)

        max_so_far = 0
        max_set = []
        for vertex in vertices:
            neigh = set()
            for vertex1 in vertices:
                if (vertex + '-' + vertex1) in edges or (vertex1 + '-' + vertex) in edges:
                    neigh.add(vertex1)
            assert len(neigh) == 13

            for i in range(max_so_far, 14):
                for x in itertools.combinations(neigh, i):
                    if all([(pair[0] + '-' + pair[1]) in edges or (pair[1] + '-' + pair[0]) in edges for pair in itertools.combinations(x, 2)]):
                        max_so_far = i + 1
                        max_set = list(x)
                        max_set.append(vertex)
        max_set.sort()
        print('Part Two: ', ','.join(max_set))


if __name__ == "__main__":
    main()
