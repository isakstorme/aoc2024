from collections import deque

with open("input/input9.txt") as file:
    line = file.read().splitlines()[0]

#line = "2333133121414131402"

def parseinput(line):
    memory = []
    index = 0
    for i in range(len(line)):
        nbr = int(line[i])   #nbr of positions that shall be occupied either by . or the index
        if i % 2 == 0:
            for j in range(nbr):
                memory.append(str(index))
        elif i % 2 == 1:
            for j in range(nbr):
                memory.append(".")
            index += 1
    return memory

def parseinput2(line):  # returns a dictionary where key is index and value is a pair (startindex, size). Also returns free_spaces, a list of tuples (startindex, size)
    file_sizes = dict()
    free_spaces = []
    index = 0
    memory_index = 0 # starting position of where file is stored in memory
    for i in range(len(line)):
        nbr = int(line[i])  # nbr of positions that shall be occupied either by . or the index
        if i % 2 == 0:
            file_sizes[index] = memory_index, nbr
            memory_index += nbr
        elif i % 2 == 1:
            free_spaces.append((memory_index, nbr))
            memory_index += nbr
            index += 1
    return file_sizes, free_spaces

def occupy_free_space(memory):  #Brute force approach first, not most effective but will try it originally
    last_free_index = 0
    for i in range(len(memory) - 1, -1, -1):  # (len - 1, len -2, ..., 2, 1, 0)
        if memory[i] != ".":
            for j in range(last_free_index, i):   # If last_free_index > i we quit the loop because otherwise the program might move memory backwards in memory.
                if memory[j] == ".":
                    memory[i], memory[j] = memory[j], memory[i]
                    last_free_index = j
                    break
    return memory
def solution1(memory):
    result = 0
    for i in range(len(memory)):
        if memory[i] == ".":
            break
        result += int(memory[i]) * i
    return result


def solution2(file_sizes, free_spaces):   #This function is quite unreadable, might make more readable
    result = 0
    keys = file_sizes.keys()
    for k in range(len(keys) - 1, -1, -1):
        for f in range(len(free_spaces)):
            start_index_file = file_sizes[k][0]
            size_file = file_sizes[k][1]
            start_index_free = free_spaces[f][0]
            size_free = free_spaces[f][1]
            if size_file <= size_free and start_index_free < start_index_file:  #Checks if there is a sufficiently large cap at a lower index.
                file_sizes[k] = start_index_free, size_file #then occupies that index
                if file_sizes[k][1] == free_spaces[f][1]:  #if the spaces are equal in size
                    free_spaces.pop(f)
                elif file_sizes[k][1] < free_spaces[f][1]:   #If the free space is larger than requred
                    free_spaces[f] = start_index_free + size_file, size_free - size_file  #Reduces the available space but does not pop because free space remains.
                break
    for i in range(len(keys)):   #counts
        startpos = file_sizes[i][0]
        size = file_sizes[i][1]
        for j in range(size):
            result += i * (startpos + j)
    return result

if __name__ == '__main__':
    p1 = solution1(occupy_free_space(parseinput(line)))
    file_sizes, free_spaces = parseinput2(line)
    p2 = solution2(file_sizes, free_spaces)
    f = open("solutions\solution9.txt", "w")
    f.write(str(p1) + ": answer 1 \n")
    f.write(str(p2) + ": answer 2 ")
    f.close()



