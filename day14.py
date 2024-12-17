with open("input/input14.txt") as file:
    lines = file.read().splitlines()

#lines = """p=0,4 v=3,-3
#p=6,3 v=-1,-3
#p=10,3 v=-1,2
#p=2,0 v=2,-1
#p=0,0 v=1,3
#p=3,0 v=-2,-2
#p=7,6 v=-1,-3
#p=3,0 v=-1,-2
#p=9,3 v=2,3
#p=7,3 v=-1,2
#p=2,4 v=2,-3
#p=9,5 v=-3,-3""".splitlines()

def solution1(lines):
    h = 103
    w = 101
    robots_pos = []  #Kanske använda dict istället
    robots_vel = []
    for l in (lines):
        p, v = l.split()
        p = tuple(map(int, p[2:].split(",")))
        v = tuple(map(int, v[2:].split(",")))
        robots_pos.append(p)
        robots_vel.append(v)

    for s in range(100):
        for n, pos in enumerate(robots_pos):
            dx, dy = robots_vel[n]
            next = (pos[0] + dx) % w, (pos[1] + dy) % h  #python modulo works well here
            robots_pos[n] = next
    #counts
    upl, upr, downl, downr = 0, 0, 0, 0
    half_h = h // 2
    half_w = w // 2
    for x, y in robots_pos:
        if x > half_w and y > half_h:
            upr += 1
        elif x < half_w and y > half_h:
            upl += 1
        elif x > half_w and y < half_h:
            downr += 1
        elif x < half_w and y < half_h:
            downl += 1
    return  upl * upr * downl * downr

print(solution1(lines))