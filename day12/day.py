import sys


def inbounds(map, pos):
    x, y = pos
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


def find_neighbors(map, pos):
    x, y = pos
    neighbors = set()
    for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if not inbounds(map, (x2, y2)):
            continue
        if map[y2][x2] == map[y][x]:
            neighbors.add((x2, y2))
    return neighbors


def dfs(visited, neighbors, pos):
    if pos not in visited:
        visited.add(pos)
        for neighbor in neighbors[pos]:
            dfs(visited, neighbors, neighbor)
    return visited


data = open('day12.txt', 'r').read().strip().split("\n")
neighbors = {}

for y, line in enumerate(data):
    for x, char in enumerate(line):
        matching_neighbors = find_neighbors(data, (x, y))
        neighbors[(x, y)] = matching_neighbors


def count_common_sides(region):
    ct = 0
    for x, y in region:
        if (x - 1, y) in region:
            for y2 in [y - 1, y + 1]:
                if (x, y2) not in region and (x - 1, y2) not in region:
                    ct += 1
        if (x, y - 1) in region:
            for x2 in [x - 1, x + 1]:
                if (x2, y) not in region and (x2, y - 1) not in region:
                    ct += 1
    return ct


p1 = p2 = 0
regions = []
seen = set()
for pos, cur_neighbors in neighbors.items():
    if pos in seen:
        continue
    region = dfs(set(), neighbors, pos)
    area = len(region)
    perimeter = sum([4 - len(neighbors[(x, y)]) for x, y in region])
    p1 += area * perimeter
    p2 += area * (perimeter - count_common_sides(region))
    print(pos[1], pos[0], data[pos[1]][pos[0]], area, (perimeter - count_common_sides(region)))
    seen.update(region)
    regions.append(region)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")