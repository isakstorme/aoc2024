with open("input/input19.txt") as file:
    available, requested = file.read().split("\n\n")
    available = available.split(", ")
    requested = requested.splitlines()

#available = "r, wr, b, g, bwu, rb, gb, br".split(", ")
#requested = """brwrr
#bggr
#gbbr
#gbbr
#rrbgbr
#ubwu
#bwurrg
#brgr
#bbrgwb""".splitlines()

def solution1(requested, available):
    result = 0
    cache = dict()
    for r in requested:
        def dfs(string, available):
            if string == "":
                return True
            elif string in cache:
                return cache[string]
            true_or_false = False
            for a in available:
                length = len(a)
                if string[:length] == a:
                    true_or_false = (dfs(string[length:], available))
                    if true_or_false:
                        break
            if true_or_false:
                cache[string] = True
                return True
            cache[string] = False    # I accidentally had cache[r] on both of these, then figured out I should change one. Then took me half an hour. Then decided I should check next one as well.
            return False
        if dfs(r, available):
            result += 1
    return result

def solution2(requested, available):
    result = 0
    cache = dict()
    for r in requested:
        def dfs(string, available):
            if string == "":
                return 1
            elif string in cache:
                return cache[string]
            result = 0
            for a in available:
                length = len(a)
                if string[:length] == a:
                    result += (dfs(string[length:], available))
                    cache[string] = result
            return result
        result += dfs(r, available)
    return result

if __name__ == '__main__':
    print(solution1(requested, available))
    print(solution2(requested, available))