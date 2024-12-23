with open("input/example22.txt") as file:
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
        value = last_digit(n)
        seq = []  # current sequence
        for r in range(2000):
            #print(seq)
            n = algorithm(n)
            seq.append(last_digit(n) - value)
            value = last_digit(n)
            if seq == [-2,1,-1,3]:
                print(value)
            if len(seq) == 4:
                #print(seq)
                if tuple(seq) not in seq_dict:
                    seq_dict[tuple(seq)] = value
                elif value > seq_dict[tuple(seq)]:
                    seq_dict[tuple(seq)] = value
                seq = []
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
