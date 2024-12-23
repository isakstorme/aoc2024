with open("input/input23.txt") as file:
    lines = file.read().splitlines()


def is_connected(k, k2, k3, edges):
    if (k in edges[k2] or k2 in edges[k]) and (k in edges[k3] or k3 in edges[k]) and (k2 in edges[k3] or k3 in edges[k2]):
        return True
    return False


def solution1(lines):
    groups_of_3 = set()
    edges = dict()
    for l in lines:
        l1, l2 = l.split("-")
        if not l1 in edges.keys():
            edges[l1] = {l2}
        else:
            edges[l1].add(l2)
        if not l2 in edges.keys():
            edges[l2] = {l1}
        else:
            edges[l2].add(l1)

    for k in edges.keys():
        for k2 in edges[k]:
            for k3 in edges[k2]:
                if k in edges[k3] or k3 in edges[k]:
                    s = tuple(sorted([k, k2, k3]))
                    groups_of_3.add(s)
    result = 0
    for g in groups_of_3:
        for e in g:
            if e[0] == "t":
                result += 1
                break
    return result


def find_max_group(edges):    #This solutions seems quite ineffective. Uses a seen set to decrease redundant calculations. I could probably minimize redundant calculations further.
    group = []
    V = edges.keys()
    seen = set()
    def helper(g, edges):
        nonlocal group
        for e in g:
            for e2 in g:
                if not e2 in edges[e] and not e in edges[e2] and not e == e2:
                    return
        if len(g) > len(group):
            group = g
        for e in edges[g[0]]:
            if e in g:
                continue
            if frozenset(g + [e]) in seen:
                continue
            seen.add(frozenset(g + [e]))
            helper(g + [e], edges)
    for v in V:
        helper([v], edges)
    return sorted(group)



def solution2(lines):
    groups = []
    edges = dict()
    for l in lines:
        l1, l2 = l.split("-")
        if l1 not in edges.keys():
            edges[l1] = {l2}
        else:
            edges[l1].add(l2)
        if l2 not in edges.keys():
            edges[l2] = {l1}
        else:
            edges[l2].add(l1)

    group = find_max_group(edges)
    return group
if __name__ == '__main__':
    p1 = solution1(lines)
    print(p1)
    p2 = solution2(lines)
    print(p2)
