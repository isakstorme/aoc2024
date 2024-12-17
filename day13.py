import heapq

with open("input/input13.txt") as file:
    exercises = file.read().split("\n\n")

#exercises = """Button A: X+94, Y+34
#Button B: X+22, Y+67
#Prize: X=8400, Y=5400

#Button A: X+26, Y+66
#Button B: X+67, Y+21
#Prize: X=12748, Y=12176

#Button A: X+17, Y+86
#Button B: X+84, Y+37
#Prize: X=7870, Y=6450

#Button A: X+69, Y+23
#Button B: X+27, Y+71
#Prize: X=18641, Y=10279""".split("\n\n")

# Is there something inefficient here, should I handle visited coordinates different. Or should I handle when to add to heap differently?
def dijkstras(adx, ady, bdx, bdy, targetx, targety):   #slightly modified dihj´´jkstras
    costs = dict()
    x, y = 0, 0
    costs[(0, 0)] = 0
    heap = [(0, (0, 0))]
    visited = set()
    while True:
        x, y = heapq.heappop(heap)[1]
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if costs[(x, y)] > 400:
            return 0    #No path within required number of steps
        if (x, y) == (targetx, targety):
            return costs[(x, y)]
        a_next = x + adx, y + ady
        b_next = x + bdx, y + bdy
        if a_next not in visited:
            if not a_next in costs.keys() or costs[a_next] > costs[(x, y)] + 3:
                costs[a_next] = costs[(x, y)] + 3
                heapq.heappush(heap, (costs[a_next], a_next))
        if b_next not in visited:
            if not b_next in costs.keys() or costs[b_next] > costs[(x, y)] + 1:
                costs[b_next] = costs[(x, y)] + 1
                heapq.heappush(heap, (costs[b_next], b_next))

def solution1(exercises):
    result = 0
    for e in exercises:
        split_e = e.split()
        adx = int(split_e[2][2:].replace(",", ""))
        ady = int(split_e[3][2:].replace(",", ""))
        bdx = int(split_e[6][2:].replace(",", ""))
        bdy = int(split_e[7][2:].replace(",", ""))
        targetx = int(split_e[9][2:].replace(",", ""))
        targety = int(split_e[10][2:])
        result += dijkstras(adx, ady, bdx, bdy, targetx, targety)
    return result

def solution1improved(exercises):  #Much more efficient than solution1. Solves the quation system with cramers rule.
    result = 0
    for e in exercises:
        split_e = e.split()
        adx = int(split_e[2][2:].replace(",", ""))
        ady = int(split_e[3][2:].replace(",", ""))
        bdx = int(split_e[6][2:].replace(",", ""))
        bdy = int(split_e[7][2:].replace(",", ""))
        targetx = int(split_e[9][2:].replace(",", ""))
        targety = int(split_e[10][2:])
        if adx * bdy - ady * bdx != 0:
            y = (adx * targety - ady * targetx) / (adx * bdy - bdx * ady)  # Uses Cramers theorem but could have solved the equation system with Gaussian elimination and used the obtained expessions for y and x as well
            x = (targetx * bdy - targety * bdx) / (adx * bdy - bdx * ady)
            if y == int(y) and x == int(x):
                result += y + 3*x
        else:
            print("linearly dependent")
            continue


    return result

def solution2(exercises):  #Much more efficient than solution1. Solves the quation system with cramers rule.
    result = 0
    for e in exercises:
        split_e = e.split()
        adx = int(split_e[2][2:].replace(",", ""))
        ady = int(split_e[3][2:].replace(",", ""))
        bdx = int(split_e[6][2:].replace(",", ""))
        bdy = int(split_e[7][2:].replace(",", ""))
        targetx = int(split_e[9][2:].replace(",", "")) + 10000000000000
        targety = int(split_e[10][2:]) + 10000000000000
        if adx * bdy - ady * bdx != 0:
            y = (adx * targety - ady * targetx) / (adx * bdy - bdx * ady)  # Uses Cramers theorem but could have solved the equation system with Gaussian elimination and used the obtained expessions for y and x as well
            x = (targetx * bdy - targety * bdx) / (adx * bdy - bdx * ady)
            if y == int(y) and x == int(x):
                result += y + 3*x
        else:
            print("linearly dependent")
            continue


    return result




 # adx, ady, bdx and bdy are the coefficients of a linear equation system. If (adx, ady) and (bdx, bdy) are linearly dependent there are either 0 or infinetely many solutions.
#def gauss(adx, ady, bdx, bdy, targetx, targety):
#    x, y = 0, 0
#    if adx * bdy - ady * bdx != 0:  #if (adx, ady) and (bdx, bdy) are linearly independent, the determinant != 0
#        k = ady / adx
#        targety -= targetx * k
#        y = targety / (bdy - k*bdx)
#        x = (targetx - bdx*y)/adx
#        return x, y

# might do a gaussian solver at some point but not now.


if __name__ == '__main__':
    print(solution1improved(exercises))
    print(solution2(exercises))
    #print(gauss(3, 1, 7, 3, 2, 4))
