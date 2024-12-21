from collections import deque

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
        adj = [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if pos[0] + d[0] in range(h) and pos[1] + d[1] in range(w)]
        for r, c in adj:
            if (grid[r][c] == "." or grid[r][c] == "E") and (r, c) not in visited:
                pos = r, c
        if pos == e:
            path.append(pos)
            break
    for n, p in enumerate(path):
        costs[p] = len(path) - n - 1
    result = 0
    for pos in path:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        adj = [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if pos[0] + d[0] in range(h) and pos[1] + d[1] in range(w)]
        for r, c in adj:
            adj2 = [(r + d[0], c + d[1]) for d in dirs if r + d[0] in range(h) and c + d[1] in range(w)]
            for r2, c2 in adj2:  #Tries the cheat
                if (r2, c2) in costs and costs[(r2, c2)] + 2 < costs[pos] - 99:  #2 because cheat equals two steps
                    result += 1
    return result

def solution2(grid):
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
        adj = [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if pos[0] + d[0] in range(h) and pos[1] + d[1] in range(w)]
        for r, c in adj:
            if (grid[r][c] == "." or grid[r][c] == "E") and (r, c) not in visited:
                pos = r, c
        if pos == e:
            path.append(pos)
            break
    for n, p in enumerate(path):
        costs[p] = len(path) - n - 1
    result = 0
    for pos in path:
        def adj(pos):
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            return [(pos[0] + d[0], pos[1] + d[1]) for d in dirs if pos[0] + d[0] in range(h) and pos[1] + d[1] in range(w)]

        visited = set()
        def check_cheat(cost, pos): #cost is the cost without cheating. This method is inspired by bfs
            q = deque([pos])
            result = 0
            counter = 0
            left_in_step = 1
            while len(q) != 0 and counter <= 20:  #check if limit is correct
                pos = q.popleft()
                if pos in costs and costs[pos] + counter < cost - 99:
                    result += 1
                for a in adj(pos):
                    if a not in visited:
                        q.append(a)
                        visited.add(a)
                left_in_step -= 1
                if left_in_step == 0:
                    counter += 1
                    left_in_step = len(q)
            return result

        result += check_cheat(costs[pos], pos)

    return result



if __name__ == '__main__':
    print(solution1(grid))
    print(solution2(grid))

