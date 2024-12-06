import cmath

with open("input/input6.txt") as file:
    grid = file.read().splitlines()


# up is 1, right is i, down is -1 and left is -i

def next_pos(dir, pos):
    next = pos
    if dir == 1:
        next = (pos[0] - 1, pos[1])
    elif dir == 1j:
        next = (pos[0], pos[1] + 1)
    elif dir == -1:
        next = (pos[0] + 1, pos[1])
    elif dir == -1j:
        next = (pos[0], pos[1] - 1)
    return next

def solution1(grid):
    h = len(grid)
    w = len(grid[0])
    pos = (0, 0)  # (r, c)
    dir = 1
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                pos = (r, c)
                dir = 1
            elif grid[r][c] == ">":
                pos = (r, c)
                dir = 1j
            elif grid[r][c] == "^":
                pos = (r, c)
                dir = -1
            elif grid[r][c] == ">":
                pos = (r, c)
                dir = -1j
    while True:
        next = next_pos(dir, pos)
        r, c = next[0], next[1]
        if not 0 <= r <= h - 1 or not 0 <= c <= w - 1:  #breaks if we are going outdide of the grid
            break
        elif grid[r][c] == "#":
            dir = dir * 1j
        else:
            pos = next
            visited.add(pos)
    return len(visited)

def solution2_helper(grid): #returns all coordinates on path, Identical to solution1 except the last line
    h = len(grid)
    w = len(grid[0])
    pos = (0, 0)  # (r, c)
    dir = 1
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                pos = (r, c)
                dir = 1
            elif grid[r][c] == ">":
                pos = (r, c)
                dir = 1j
            elif grid[r][c] == "^":
                pos = (r, c)
                dir = -1
            elif grid[r][c] == ">":
                pos = (r, c)
                dir = -1j
    while True:
        next = next_pos(dir, pos)
        r, c = next[0], next[1]
        if not 0 <= r <= h - 1 or not 0 <= c <= w - 1:  # breaks if we are going outdide of the grid
            break
        elif grid[r][c] == "#":
            dir = dir * 1j
        else:
            pos = next
            visited.add(pos)
    return visited

def solution2(grid):
    h = len(grid)
    w = len(grid[0])
    pos = (0, 0)  # (r, c)
    dir = 0
    visited = set()
    cycles = 0
    starting_pos = (0, 0)
    starting_dir = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "^":
                starting_pos = (r, c)
                starting_dir = 1
            elif grid[r][c] == ">":
                starting_pos = (r, c)
                starting_dir = 1j
            elif grid[r][c] == "^":
                starting_pos = (r, c)
                starting_dir = -1
            elif grid[r][c] == ">":
                starting_pos = (r, c)
                starting_dir = -1j
    for coordinate in solution2_helper(grid):   # Tests to add obstruction on every possible coordinate
        obstruction = coordinate
        pos = starting_pos
        dir = starting_dir
        while True:
            next = next_pos(dir, pos)
            r, c = next[0], next[1]
            if not 0 <= r <= h - 1 or not 0 <= c <= w - 1:  #breaks if we are going outdide of the grid, no cycle detected
                visited = set()
                break
            elif grid[r][c] == "#" or (r, c) == obstruction:
                dir = dir * 1j
            else:
                pos = next
                if (pos[0], pos[1], dir) in visited:
                    cycles += 1   #cycle detected because we have already been at that coordinate and been going in the same direction
                    visited = set()
                    break
                visited.add((pos[0], pos[1], dir))

    return cycles

if __name__ == '__main__':
    result1 = solution1(grid)
    result2 = solution2(grid)
    f = open("solutions\solution6.txt", "w")
    f.write(str(result1) + ": answer 1 \n")
    f.write(str(result2) + ": answer 2 ")
    f.close()
