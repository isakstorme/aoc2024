#inspired by day 5, very simple example

from functools import cmp_to_key

order = {"a": {"b", "c"}, "b": {"c"}}

def compare(x1, x2):
    if x1 in order and x2 in order[x1]:
        return -1
    if x2 in order and x1 in order[x2]:
        return 1
    return 0

print(sorted(["b", "c", "a"], key= cmp_to_key(compare)))