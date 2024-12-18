import heapq

with open("input/input18.txt") as file:
    lines = file.read().splitlines()



def adj4(pos, h, w):
    ret = []
    for t in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if pos[0] + t[0] in range(h) and pos[1] + t[1] in range(w):
            ret.append((pos[0] + t[0], pos[1] + t[1]))
    return ret


def bfs(grid):
    h = len(grid)
    w = len(grid)
    pos = 0, 0
    target = h - 1, w - 1
    heap = [(0, (0, 0))]
    added = {(0, 0)}
    costs = {(0, 0): 0}
    while len(heap) > 0:
        pos = heapq.heappop(heap)[1]
        if pos == target:
            return costs[pos]
        for r, c in adj4(pos, h, w):
            if grid[r][c] != "x" and (r, c) not in added:
                costs[(r, c)] = costs[pos] + 1
                heapq.heappush(heap, (costs[(r, c)], (r, c)))
                added.add((r, c))
    return 0 # no path found



def solution1(lines, nbr_bytes):
    h, w = 70, 70
    grid = [["," for c in range(w + 1)] for r in range(h + 1)]
    for n, l in enumerate(lines):
        r, c = l.split(",")
        r, c = int(r), int(c)
        if n < nbr_bytes:
            grid[r][c] = "x"
    cost = bfs(grid)
    return cost

def solution2(lines):
    nbr = len(lines) // 2   #the interval needed to check
    interval_size = len(lines) // 2
    highest_possible = -1
    dir = 0
    while interval_size > 0:
        sol = solution1(lines, nbr)
        if sol == 0:   #If no path exists
             dir = -1
        else:  #if path exists
            highest_possible = nbr
            dir = 1

        interval_size = interval_size // 2
        nbr = nbr + dir * interval_size

    first_impossible = highest_possible
    return lines[first_impossible]




if __name__ == '__main__':
    print(solution1(lines, 1024))
    print(solution2(lines))