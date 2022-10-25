def char0str():
    arr = ['a', 'b', 'c', 'd']

    x = ' '

    i = 0

    for _ in arr:
        x = x[:i] + _
        i += 1

    return x

print(char0str())