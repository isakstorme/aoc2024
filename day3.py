import re

with open("input\input3.txt") as input:
    lines = input.read()

def parsemul(mul): # parses mul({nbr1},{nbr2})
    muls = mul.split(",")
    nbr1 = "".join(c for c in muls[0] if c.isdigit())
    nbr2 = "".join(c for c in muls[1] if c.isdigit())
    return int(nbr1) * int(nbr2)

def solution1(lines):
    pattern = "mul\(\d+,\d+\)"
    muls = re.findall(pattern, lines)
    return sum(map(parsemul, muls))

def solution2(lines):
    pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
    ops = re.findall(pattern, lines)
    result = 0
    enabled = True;
    for i in range(len(ops)):
        if ops[i] == "do()":
            enabled = True
        elif ops[i] == "don't()":
            enabled = False
        else:
            if enabled:
                result += parsemul(ops[i])

    return result




if __name__ == '__main__':
    result1 = solution1(lines)
    result2 = solution2(lines)
    f = open("solutions\solution3.txt", "w")
    f.write(str(result1) + ": answer 1 \n")
    f.write(str(result2) + ": answer 2 ")
    f.close()