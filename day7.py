from math import perm
with open("input/input7.txt") as file:
    lines = file.read().splitlines()

#lines = "190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20".splitlines()


#In this file I try without itertools but maybe I will try with it as well.
def recursive_search(ints, index, result, test_score):
    if index == len(ints) - 1:
        last = ints[len(ints) - 1]
        if result + last == test_score or result * last == test_score:
            return test_score
        else:
            return 0
    mul = recursive_search(ints, index + 1, result * ints[index], test_score)
    add = recursive_search(ints, index + 1, result + ints[index], test_score)
    if mul == test_score or add == test_score:
        return test_score
    return 0

def recursive_search2(ints, index, result, test_score):
    if index == 0:
        result = ints[0]
    if index == len(ints) - 1:
        last = ints[len(ints) - 1]
        if result + last == test_score or result * last == test_score or int(str(result) + str(last)) == test_score:
            return test_score
        else:
            return 0
    mul = recursive_search2(ints, index + 1, result * ints[index], test_score) #took a long time to realize the type forgot to add a 2
    add = recursive_search2(ints, index + 1, result + ints[index], test_score)
    concat_nbr = int(str(result) + str(ints[index]))
    if test_score == 156:
        print(concat_nbr)
    ints = ints[:index - 1] + [concat_nbr] + ints[index + 1:]
    concat = recursive_search2(ints, index, concat_nbr, test_score)
    if mul == test_score or add == test_score or concat == test_score:
        return test_score
    return 0

def solution1(lines):
    result = 0
    for l in lines:
        test_score, ints = l.split(":")
        test_score = int(test_score)
        ints = list(map(int, ints.split()))
        result += recursive_search(ints, 1, ints[0], test_score)
    return result

def solution2(lines):
    result = 0
    for l in lines:
        test_score, ints = l.split(":")
        test_score = int(test_score)
        ints = ints.split()
        ints = list(map(int, ints))
        result += recursive_search2(ints, 1, ints[0], test_score)
    return result


if __name__ == '__main__':
    ans1 = solution1(lines)
    print(ans1)
    ans2 = solution2(lines)
    print(ans2)