import sys

with open("input/input12.txt") as file:
    grid = file.read().splitlines()


#grid = """RRRRIICCFF
#RRRRIICCCF
#VVRRRCCFFF
#VVRCCCJFFF
#VVVVCJJCFE
#VVIVCCJJEE
#VVIIICJJEE
#MIIIIIJJEE
#MIIISIJEEE
#MMMISSJEEE""".splitlines()


#grid = """AAAAAA
#AAABBA
#AAABBA
#ABBAAA
#ABBAAA
#AAAAAA""".splitlines()

# grid = """AAAA
# BBCD
# BBCC
# EEEC""".splitlines()

# grid = """OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO""".splitlines()

# grid = """EEEEE
# EXXXX
# EEEEE
# EXXXX
# EEEEE""".splitlines()


def adj(r, c):
    ret = []
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ret.append((r + dr, c + dc))
    return ret


def perimeter(coordinates):  # group of connected coordinates, returns number of sides
    result = 0
    for r, c in coordinates:
        result += 4
        ns = adj(r, c)
        for rr, cc in ns:
            if (rr, cc) in coordinates:
                result -= 1
    return result


def solution1(grid):
    h = len(grid)
    w = len(grid[0])
    groups = []
    visited = set()
    for r in range(h):
        for c in range(w):

            def dfs(r, c):
                if (r, c) in visited:
                    return set()
                visited.add((r, c))
                type = grid[r][c]
                ret = {(r, c)}
                for rr, cc in adj(r, c):
                    if rr in range(h) and cc in range(w) and grid[rr][cc] == type:
                        ret = ret.union(dfs(rr, cc))
                return ret

            group = dfs(r, c)
            groups.append(group)
    result = 0
    for g in groups:
        result += len(g) * perimeter(g)
    return result


def partitions(group):  # sorted group
    partitions = [[group[0]]]
    partition_nbr = 0
    for i in range(len(group) - 1):
        current = group[i]
        next = group[i + 1]
        if current + 1 == next:
            partitions[partition_nbr].append(next)
        else:
            partitions.append([next])
            partition_nbr += 1
    return partitions


def is_overlap(p2, current):
    if min(p2) in current and max(p2) in current:
        return True
    return False

def under(below, above):
    ret = []

    for part in below:
        for p in part:
            if min(above)<=p<=max(above):
                ret += part

    return ret

def nbr_sides2(coordinates):  # fence_cost for part 2, this function is atrocious, todo, write a better version
    l = len(coordinates)
    coordinates = list(coordinates)
    coordinates.sort()  # sorted by r
    groups = [[]]
    current_r = coordinates[l - 1][0]  # Starting to pop backwards, that's why I start with the last element
    group_nbr = 0
    for i in range(l):
        coordinate = coordinates.pop()
        if coordinate[0] == current_r:
            groups[group_nbr].append(coordinate[1])
        else:
            current_r = coordinate[0]
            group_nbr += 1
            groups.append([coordinate[1]])
    groups = list(map(lambda g: sorted(g), groups))
    result = 4 * len(partitions(groups[0]))  # 4 is the minimum number of lines and for each iteration we add if necessary
    for g_nbr in range(len(groups) - 1):
        current, next = groups[g_nbr], groups[g_nbr + 1]
        current_parts, next_parts = partitions(current), partitions(next)
        if current == next:
            continue

        for p1 in next_parts:
            under1 = under(current_parts, p1)
            if under1 != []:
                if max(under1) == max(p1):
                    result -= 2
                if min(under1) == min(p1):
                    result -= 2
            result += 4
    return result


def solution2(grid):
    h = len(grid)
    w = len(grid[0])
    groups = []
    visited = set()
    for r in range(h):
        for c in range(w):

            def dfs(r, c):
                if (r, c) in visited:
                    return set()
                visited.add((r, c))
                type = grid[r][c]
                ret = {(r, c)}
                for rr, cc in adj(r, c):
                    if rr in range(h) and cc in range(w) and grid[rr][cc] == type:
                        ret = ret.union(dfs(rr, cc))
                return ret

            group = dfs(r, c)  # Kanske endast köra nästa rad om group inte är tom
            if len(group) > 0:
                groups.append(group)
    result = 0
    for g in groups:
        result += len(g) * nbr_sides2(g)
    return result


if __name__ == '__main__':
    p1 = solution1(grid)
    print(p1)
    p2 = solution2(grid)
    print(p2)
