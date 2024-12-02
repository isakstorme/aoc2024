with open("input\input2.txt") as input:
    lines = input.read().splitlines()


def solution1(lines):
    result = 0
    for l in lines:
        xs = list(map(int, l.split()))
        if is_correct(xs):
            result += 1
    return result


def is_correct(xs):  # xs is a list of ints
    dir = -1
    error_found = False
    if xs[0] > xs[1]:  # If the list of numbers decrease dir = 1 else dir = -1
        dir = 1
    for i in range(len(xs) - 1):
        # This could probably be made more readable but checks that the list either increases and decreases and that the difference is 1<=d<=3
        if (xs[i] - xs[i + 1]) * dir > 3 or (xs[i] - xs[i + 1]) * dir < 1:
            error_found = True
            break
    return not error_found


def solution2(lines):
    result = 0
    for l in lines:
        xs = l.split()
        xs = list(map(int, xs))
        dir = -1
        error_found = False
        if xs[0] > xs[1]:
            dir = 1
        for i in range(len(xs) - 1):
            if (xs[i] - xs[i + 1]) * dir > 3 or (xs[i] - xs[i + 1]) * dir < 1:
                #If error is detected we check if it is possible to remove the number itself or one of the two adjacent numbers
                s1 = xs[:i] + xs[i + 1:]
                s2 = xs[:i + 1] + xs[i + 2:]
                s3 = xs[:i - 1] + xs[i:]
                if not (is_correct(s1) or is_correct(s2) or is_correct(s3)):
                    error_found = True
                break  # took a long time to realise break is necessary: for example 5 7 4 3 2 could not be detected otherwise becuase the for loop would continue considering the following numbers with the expectation that they go uo.

        if not error_found:
            result += 1
    return result


if __name__ == '__main__':
    result1 = solution1(lines)
    result2 = solution2(lines)
    f = open("solutions\solution2.txt", "w")
    f.write(str(result1) + ": answer 1 \n")
    f.write(str(result2) + ": answer 2 ")
    f.close()
