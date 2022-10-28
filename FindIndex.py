def findIndex(n, k):
    s = 0
    l = []

    if k not in n:
        return -1, -1

    while s < len(n):
        if n[s] == k:
            l.append(s)
        s += 1

    return min(l), max(l)

print(findIndex([1, 2, 3, 4, 5, 5], 5))