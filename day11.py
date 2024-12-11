import sys

with open("input/input11.txt") as file:
    stones = list(map(int, file.read().split()))

#stones= [125, 17]
sys.setrecursionlimit(100000)


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

cache = {}
def helper(x, n):
    if (x, n) in cache:
        return cache[(x, n)]
    if n == 0:
        return 1
    result = 0
    next_stones = rules(x)
    if len(next_stones) == 1:
        result = helper(next_stones[0], n-1)
    elif len(next_stones) == 2:
        result = helper(next_stones[0], n-1) + helper(next_stones[1], n-1)
    cache[(x, n)] = result
    return result

def solution2(stones):
    result = 0
    for s in stones:
        result += helper(s, 75)
    return result



if __name__ == '__main__':
    p1 = solution1(stones)
    print(p1)
    p2 = solution2(stones)
    print(p2)
