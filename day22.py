with open("input/input22.txt") as file:
    ints = list(map(int, file.read().splitlines()))


def mix(n, n2):
    return n ^ n2


def prune(n):
    return n % 16777216


def algorithm(n):
    # step 1
    n = mix(n, n * 64)
    n = prune(n)
    # step 2
    n = mix(n, n // 32)
    n = prune(n)
    # step 3
    n = mix(n, n * 2048)
    n = prune(n)
    return n


def solution1(ints):
    result = 0
    for i in ints:
        n = i
        for r in range(2000):
            n = algorithm(n)
        result += n
    return result


def last_digit(n):
    n = str(n)
    return int(str(n)[len(n) - 1])


def solution2(ints):
    result = 0
    seqs = dict()
    for i in ints:
        seq_dict = dict()
        n = i
        seq_list = [[], [], [], []]  # current sequence
        delay = 3
        value = last_digit(i)
        for r in range(2000):
            #print(seq)
            n = algorithm(n)
            seq_list[0].append(last_digit(n) - value)
            if delay < 3:
                seq_list[1].append(last_digit(n) - value)
            if delay < 2:
                seq_list[2].append(last_digit(n) - value)
            if delay < 1:
                seq_list[3].append(last_digit(n) - value)
            value = last_digit(n)
            for n1, seq in enumerate(seq_list):
                if len(seq) == 4:
                    if tuple(seq) not in seq_dict:
                        seq_dict[tuple(seq)] = value
                    #elif value > seq_dict[tuple(seq)]:  #This was a bug, if a sequence has been detected it can't happen again!
                    #    seq_dict[tuple(seq)] = value
                    seq_list[n1] = []
            if delay > 0:
                delay -= 1
        for s in seq_dict.keys():
            if s in seqs:
                seqs[s] += seq_dict[s]
            else:
                seqs[s] = seq_dict[s]

        result = max(seqs.values())
    return result


if __name__ == '__main__':
    # print(solution1(ints))
    print(solution2(ints))
