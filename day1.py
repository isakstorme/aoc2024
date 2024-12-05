with open("input\input1.txt") as input:
    lines = input.read().splitlines()


xs = []
ys = []
#probably better to add like in a heap, might change later if I feel like it
for l in lines:
    split_l = l.split("   ")
    xs.append(int(split_l[0]))
    ys.append(int(split_l[1]))

xs.sort()
ys.sort()

result1 = 0
for i in range(len(xs)):
    result1 += abs(xs[i] - ys[i])

# End of challenge 1
result2 = 0
for x in xs:
    for y in ys: #Really bad time complexity, probably O(n^2) In actual fact it would be sufficient to stop looking if y >= x.
        if x == y:
            result2 += x

f = open("solutions\solution1.txt", "w")
f.write(str(result1) + ": answer 1 \n")
f.write(str(result2) + ": answer 2 ")
f.close()