with open("input/input20.txt") as file:
    grid = file.read().splitlines()

#grid = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()


def solution1(grid):
    h = len(grid)
    w = len(grid[0])
    s = 0, 0
    e = 0, 0
    visited = set()
    pos = 0, 0
    path = []
    costs = dict()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "S":
                s = r, c
                pos = s
            elif grid[r][c] == "E":
                e = r, c
    while True:
        visited.add(pos)
        path.append(pos)
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        adj = [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if r + d[0] in range(h) and c + d[1] in range(w)]
        for r, c in adj:
            if (grid[r][c] == "." or grid[r][c] == "E") and (r, c) not in visited:
                pos = r, c
        if pos == e:
            path.append(pos)
            break
    for n, p in enumerate(path):
        costs[p] = len(path) - n - 1
    visited = set()
    pos = s
    result = 0
    print(costs)
    while True:
        visited.add(pos)
        path.append(pos)
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        adj = [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if r + d[0] in range(h) and c + d[1] in range(w)]
        for r, c in adj:
            adj2 = [(r + d[0], c + d[1]) for d in dirs if r + d[0] in range(h) and c + d[1] in range(w)]
            for r2, c2 in adj2:  #Tries the cheat
                if (r2, c2) in costs and costs[(r2, c2)] + 2 <= costs[pos] - 99:  #2 because cheat equals two steps
                    result += 1
            if (grid[r][c] == "." or grid[r][c] == "E") and (r, c) not in visited:
                pos = r, c
        if pos == e:
            break
    return result



if __name__ == '__main__':
    print(solution1(grid))

