with open("input/input15.txt") as file:
    grid, instructions = file.read().split("\n\n")
    grid = grid.splitlines()
    h = len(grid)
    w = len(grid[0])
    grid = [[grid[r][c] for c in range(w) if grid[r][c] != "\n"] for r in range(h) ]   # order of for loops matters
    instructions = instructions.replace("\n", "")   # I had a bug without this line. Then it worked on the tests but for the real data the \n-string caused trouble.

#grid = """##########
##..O..O.O#
##......O.#
##.OO..O.O#
##..O@..O.#
##O#..O...#
##O..O..O.#
##.OO.O.OO#
##....O...#
###########""".splitlines()

#instructions = """<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
#vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
#><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
#<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
#^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
#^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
#>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
#<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
#^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
#v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
#h = len(grid)
#w = len(grid[0])
#grid = [[grid[r][c] for c in range(w)] for r in range(h)]



def solution1(grid, instructions):
    h = len(grid)
    w = len(grid[0])
    wall = "#"
    box = "O"
    result = 0
    nothing = "."
    pos = (0, 0)
    dir = (0, 0)
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "@":
                pos = r, c
    for i in instructions: #I don't know why my solution does not work when it works on the tests.
        if i == "v":
            dir = (1, 0)
        elif i == "<":
            dir = (0, -1)
        elif i == "^":
            dir = (-1, 0)
        elif i == ">":
            dir = (0, 1)
        ## now checks if it is possible to go
        rr, cc = pos[0] + dir[0], pos[1] + dir[1]
        if grid[rr][cc] == nothing:
            grid[rr][cc], grid[pos[0]][pos[1]] = "@", "."
            pos = rr, cc
        elif grid[rr][cc] == wall:
            continue
        elif grid[rr][cc] == box:
            move_r, move_c = rr, cc
            while grid[move_r][move_c] == box:   #Here I check the direction I want to move in until there either is a box or wall
                move_r, move_c = move_r + dir[0], move_c + dir[1]
            if grid[move_r][move_c] == nothing:
                grid[rr][cc], grid[pos[0]][pos[1]], grid[move_r][move_c] = "@", ".", "O"
                pos = rr, cc
            else:
                continue
    result = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == box:
                result += c + r * 100

    count = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == "O":
                count += 1

    return result
if __name__ == '__main__':
    print(solution1(grid, instructions))