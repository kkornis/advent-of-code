def calc_dist(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2


def main():
    with open("input.txt") as inputtxt:
        lines = inputtxt.readlines()

        coordinates = []
        for i, line in enumerate(lines):
            coordinates.append([int(x) for x in line.split(',')])
            assert len(coordinates[-1]) == 3
            coordinates[-1].append(i)

        distances = []
        for i, x in enumerate(coordinates):
            for j, y in enumerate(coordinates):
                if i < j:
                    distances.append([i, j, calc_dist(x, y)])
        distances.sort(key=lambda x: x[2])

        clusters = [[x] for x in coordinates]

        for k, dist in enumerate(distances):
            conn = [dist[0], dist[1]]
            new_clusters = []
            central = None
            for clust in clusters:
                if coordinates[conn[0]] not in clust and coordinates[conn[1]] not in clust:
                    new_clusters.append(clust)
                else:
                    if central is None:
                        new_clusters.append(clust)
                        central = len(new_clusters) - 1
                    else:
                        new_clusters[central].extend(clust)
            clusters = new_clusters

            if k == 999:
                sizes_for_a = [len(x) for x in clusters]

            if len(clusters) == 1:
                part_two = coordinates[dist[0]][0] * coordinates[dist[1]][0]
                break

        sizes_for_a.sort(reverse=True)

        print('Part One: ', sizes_for_a[0] * sizes_for_a[1] * sizes_for_a[2])
        print('Part Two: ', part_two)


if __name__ == "__main__":
    main()
