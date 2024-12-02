with open("input\input2.txt") as input:
    lines = input.read().splitlines()
#lines = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9".splitlines()
result = 0
for l in lines:
    sline = l.split()
    dir = -1
    errorfound = False
    if int(sline[0]) > int(sline[1]):
        dir = 1
    elif int(sline[0]) < int(sline[1]):
        dir = -1
    for i in range(len(sline) - 1):
        if (int(sline[i]) - int(sline[i+1])) * dir > 3 or (int(sline[i]) - int(sline[i+1])) * dir < 1:
            errorfound = True
    if not errorfound:
        result += 1

print(result)


# part 2
def isCorrect(s_list):
    dir = -1
    errorfound = False
    if int(s_list[0]) > int(s_list[1]):
        dir = 1
    for i in range(len(s_list) - 1):
        if (int(s_list[i]) - int(s_list[i+1])) * dir > 3 or (int(s_list[i]) - int(s_list[i+1])) * dir < 1:
            errorfound = True
    if not errorfound:
        return True
result = 0
for l in lines:
    sline = l.split()
    dir = -1
    errorfound = False
    if int(sline[0]) > int(sline[1]):
        dir = 1
    for i in range(len(sline) - 1):
        if (int(sline[i]) - int(sline[i+1])) * dir > 3 or (int(sline[i]) - int(sline[i+1])) * dir < 1:
            print(l)
            if len(sline) >= i+1:
                s1 = sline[:i] + sline[i+1:]
            if len(sline) >= i+2:
                s2 = sline[:i+1] + sline[i+2:]
            if i != 0:
                s3 = sline[:i-1] + sline[i:]
            print(s1)
            print(s2)
            print(s3)
            if not (isCorrect(s1) or isCorrect(s2) or isCorrect(s3)):
                errorfound = True
            break  # took a long time to realise break is necessary: for example 5 7 4 3 2 could not be detected otherwise becuase the for loop would continue considering the following numbers with the expectation that they go uo.

    if not errorfound:
        result += 1

print(result)
