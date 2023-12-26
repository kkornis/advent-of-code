import copy


def is_in_paths(paths, old_vertex, neighbour):
    for path in paths:
        len_path = len(path)
        for i in range(len_path - 1):
            if old_vertex == path[i] and neighbour == path[i + 1]:
                return True
    return False


def process_new_vertices(paths, graph, max_component, old_vertices):
    new_vertices = []
    for old_vertex in old_vertices:
        for neighbour in graph[old_vertex]:
            if neighbour not in max_component and not is_in_paths(paths, old_vertex, neighbour):
                max_component[neighbour] = old_vertex
                new_vertices.append(neighbour)
    return new_vertices


def get_max_component_without_path_altering(paths, graph, max_component, new_vertices):
    while len(new_vertices) > 0:
        new_vertices = process_new_vertices(paths, graph, max_component, new_vertices)
    return max_component


def modify_paths(paths, max_component):
    new_vertices = set()
    for i, path in enumerate(paths):
        we_are_in = None
        copy_path = copy.deepcopy(path)
        copy_path.reverse()
        for vertex in copy_path:
            if vertex in max_component:
                if we_are_in is None:
                    we_are_in = vertex
            if we_are_in is not None and vertex not in max_component:
                new_vertices.add(vertex)
                max_component[vertex] = (i, we_are_in)
    return max_component, new_vertices


def apply_altering(paths, path_ind, alternation_point, new_reversed_path):
    ind = paths[path_ind].index(new_reversed_path[-1])
    new_reversed_path.reverse()
    new_path = paths[path_ind][: ind] + new_reversed_path
    ind_alt_point = paths[path_ind].index(alternation_point)
    new_reversed_path = copy.deepcopy(paths[path_ind][ind_alt_point:])
    new_reversed_path.reverse()
    paths[path_ind] = new_path
    return new_reversed_path


def add_path(paths, graph, vertex1, vertex2):
    max_component: dict[str, str] = {}
    new_vertices = {vertex1}
    while len(new_vertices) > 0:
        max_component = get_max_component_without_path_altering(paths, graph, max_component, new_vertices)
        max_component, new_vertices = modify_paths(paths, max_component)
    if vertex2 not in max_component:
        return False
    else:
        new_reversed_path = [vertex2]
        key = vertex2
        while key != vertex1:
            if isinstance(key, str):
                key = max_component[key]
                new_reversed_path.append(key)
            else:
                path_ind, alternation_point = key
                new_reversed_path = apply_altering(paths, path_ind, alternation_point, new_reversed_path)
                key = alternation_point
        new_reversed_path.reverse()
        paths.append(new_reversed_path)
        return True


def is_in_component(graph: dict[str, list[str]], vertex1: str, vertex2: str) -> bool:
    paths = []
    i = 0
    go = True
    while i < 4 and go:
        go = add_path(paths, graph, vertex1, vertex2)
        i += 1
    return go


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()
        lines = [x[:-1] for x in lines]
        graph = {}
        for line in lines:
            vertex, rem = line.split(': ')
            neighbours = rem.split(' ')
            graph[vertex] = neighbours

        new_vertices = {}
        for vertex in graph:
            for neighbour in graph[vertex]:
                if neighbour not in graph:
                    if neighbour not in new_vertices:
                        new_vertices[neighbour] = []
                    new_vertices[neighbour].append(vertex)
                else:
                    graph[neighbour].append(vertex)
        graph.update(new_vertices)
        vertex_list = list(graph.keys())

        component = {vertex_list[0]}
        for k, vertex in enumerate(vertex_list[1:]):
            if is_in_component(graph, vertex_list[0], vertex):
                component.add(vertex)

        print('part a: ', len(component) * (len(graph) - len(component)))
        # print('part b: ', sum_b)


if __name__ == "__main__":
    main()
