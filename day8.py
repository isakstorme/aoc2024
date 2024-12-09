with open("input/input8.txt") as file:
    lines = file.read().splitlines()
#lines = """............
#........0...
#.....0......
#.......0....
#....0.......
#......A.....
#............
#............
#........A...
#.........A..
#............
#............""".splitlines()

def antidote_positions(p1, p2):
    dir = (p2[0] - p1[0], p2[1] - p1[1])
    n1 = p1[0] - dir[0], p1[1] - dir[1]
    n2 = p2[0] + dir[0], p2[1] + dir[1]
    return n1, n2

def solution1(lines):
    antennas = dict()
    antinodes = set()
    h = len(lines)
    w = len(lines[0])
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            char = lines[r][c]
            if char.isdigit() or char.isalpha():
                if not char in antennas:
                    antennas[char] = {(r, c)}
                else:
                    antennas[char].add((r, c))
    for key in antennas.keys():
        for p1 in antennas[key]:
            for p2 in antennas[key]:
                if p1 != p2:
                    n1, n2 = antidote_positions(p1, p2)
                    if 0<=n1[0]<w and 0<=n1[1]<h:
                        antinodes.add(n1)
                    if 0<=n2[0]<w and 0<=n2[1]<h:
                        antinodes.add(n2)
    return len(antinodes)


def antidote_positions2(p1, p2, h, w):   #for question 2
    antidotes = []
    dir = (p2[0] - p1[0], p2[1] - p1[1])
    p = p1
    while True:  #Try this with list comprehension later
        antidotes.append(p)
        p = p[0] - dir[0], p[1] - dir[1]
        if not 0<=p[0]<w or not 0<=p[1]<h:
            break
    p = p1
    while True:  #Try this with list comprehension later
        antidotes.append(p)
        p = p[0] + dir[0], p[1] + dir[1] #switch direction compared to previously
        if 0<=p[0]<w or 0<=p[1]<h:
            break
    return antidotes


def solution2(lines):
    antennas = dict()
    antinodes = set()
    h = len(lines)
    w = len(lines[0])
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            char = lines[r][c]
            if char.isdigit() or char.isalpha():
                if not char in antennas:
                    antennas[char] = {(r, c)}
                else:
                    antennas[char].add((r, c))
    for key in antennas.keys():
        for p1 in antennas[key]:
            for p2 in antennas[key]:
                if p1 != p2:
                    ns = antidote_positions2(p1, p2, h, w)
                    for n in ns:
                        antinodes.add(n)
    return len(antinodes)

if __name__ == '__main__':
    p1 = solution1(lines)
    p2 = solution2(lines)
    f = open("solutions\solution8.txt", "w")
    f.write(str(p1) + ": answer 1 \n")
    f.write(str(p2) + ": answer 2 ")
    f.close()
