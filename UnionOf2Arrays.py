def merge(l1, l2, x, y):
    l = []
    i = 0
    j = 0

    while (i < x) and (j < y):
        l.append(l1[i])
        l.append(l2[j])
        i += 1
        j += 1

    return l + l1[i:] + l2[j:]


def union():
    l1 = [85, 25, 1, 32, 54, 6]
    l2 = [85, 2]

    merged = merge(l1, l2, len(l1), len(l2))

    print(merged)

    hash_map = {}
    count = 0 

    for i, n in enumerate(merged):
        if n not in hash_map:
            hash_map[n] = i
            count += 1

    return count

print(union())