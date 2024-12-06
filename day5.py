with open("input\input5.txt") as input:
    lines = input.read().splitlines()
half = 0
for i in range(len(lines)):
    if lines[i] == "":
        half = i

rules = lines[:half]
updates = lines[half + 1:]
ruledict = dict()  # says what numbers must come before the key.
for r in rules:
    first, last = r.split("|")
    if first not in ruledict:
        ruledict[first] = {last}
    else:
        ruledict[first].add(last)


def solution1(updates, ruledict):
    p1 = 0
    for u in updates:
        is_correct = True
        u_list = u.split(",")
        for i in range(len(u_list)):
            for i1 in range(len(u_list)):
                if i1 > i and u_list[i] in ruledict[u_list[i1]]:
                    is_correct = False
                    break
        if is_correct:
            p1 += int(u_list[len(u_list) // 2])
    return p1

def solution2(updates, ruledict):   #Not sure if my sorting guarantees correct solution or if I was just lucky with the input
    p2 = 0
    for u in updates:
        is_correct = True
        u_list = u.split(",")
        for i in range(len(u_list)):  # Bubble sort, ruledict defines the order completely, input is friendly enough. You don't have to deduce a -> c if a ->b and b ->c but it is stated explicitly
            for j in range(len(u_list) - 1):
                if u_list[j] in ruledict[u_list[j + 1]]:
                    u_list[j], u_list[j + 1] = u_list[j + 1], u_list[j]
                    is_correct = False
        if not is_correct:
            p2 += int(u_list[len(u_list) // 2])
    return p2


if __name__ == '__main__':
    result1 = solution1(updates, ruledict)
    result2 = solution2(updates, ruledict)
    f = open("solutions\solution5.txt", "w")
    f.write(str(result1) + ": answer 1 \n")
    f.write(str(result2) + ": answer 2 ")
    f.close()

