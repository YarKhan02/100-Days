def delete():
    s = 'waliyarkhan'
    x = ''
    i = 0

    for _ in range(len(s)):
        if (_ % 2) == 0:
            x = x + s[_]
            i += 1

    return x

print(delete())