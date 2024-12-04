# Minsinterpreted the task.
with open("input\input4.txt") as input:
    lines = input.read().splitlines()

#lines = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX".splitlines()


def substrings(r, c, lines):  # substrings of size 4, used in exercise 1
    strings = []
    moves = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
    moves.remove((0, 0))
    for move in moves:  # Cartesian product
        substring = []
        r1 = r
        c1 = c
        for e in range(4):
            if 0 <= r1 < len(lines) and 0 <= c1 < len(lines[r1]):
                substring.append(lines[r1][c1])
                r1 += move[0]
                c1 += move[1]
            else:
                r1 = r
                c1 = c
                strings.append("".join(substring))
            if e == 3:
                r1 = r
                c1 = c
                strings.append("".join(substring))
    return strings


def solution1(lines):
    strings = []
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "X":
                strings += substrings(r, c, lines)
    return strings.count("XMAS")


def is_x(r, c, lines):
    if 0<r<len(lines) - 1 and 0<c<len(lines[r]) - 1:
        return (lines[r + 1][c + 1] + lines[r - 1][c - 1] == "SM" or lines[r + 1][c + 1] + lines[r - 1][c - 1] == "MS") and (lines[r + 1][c - 1] + lines[r - 1][c + 1] == "SM" or lines[r + 1][c - 1] + lines[r - 1][c + 1] == "MS")
    return False

def solution2(lines):
    result = 0
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "A":
                if is_x(r, c, lines):
                    result += 1
    return result


if __name__ == '__main__':
    result1 = solution1(lines)
    result2 = solution2(lines)
    f = open("solutions\solution4.txt", "w")
    f.write(str(result1) + ": answer 1 \n")
    f.write(str(result2) + ": answer 2 ")
    f.close()
