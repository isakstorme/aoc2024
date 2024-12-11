with open("input/input11.txt") as file:
    stones = list(map(int, file.read().split()))

#stones= [125, 17]


def rules(s):
    if s == 0:
        return [1]
    s = str(s)  #str to compare length
    if len(s) % 2 == 0:
        half = len(s)//2
        return [int(s[:half]), int(s[half:])]
    else:
        return [int(s) * 2024]

def solution1(stones):
    for r in range(25):
        to_add = []
        for i, s in enumerate(stones):
            new_stones = rules(s)
            to_add += new_stones
        stones = to_add
    return len(stones)

def rules2(stones):
    result = []
    for s in stones:
        if s == 0:
            result += [1]
        s = str(s)  #str to compare length
        if len(s) % 2 == 0:
            half = len(s)//2
            result += [int(s[:half]), int(s[half:])]
        else:
            result += [int(s) * 2024]
    return result

def solution2(stones):
    for r in range(75):
        to_add = []
        for i, s in enumerate(stones):
            new_stones = rules(s)
            to_add += new_stones
        stones = to_add
    return len(stones)


if __name__ == '__main__':
    p1 = solution1(stones)
    print(p1)