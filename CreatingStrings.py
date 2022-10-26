from itertools import permutations

def perm():

    s = input()

    result = sorted([''.join(_) for _ in list(set(permutations(s)))])

    print(len(result))

    for _ in result:
        print(_)

    return ''

print(perm())