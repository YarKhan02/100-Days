def check(s):
    l = len(s)

    if l <= 1:
        return 'YES'

    if s[0] == s[1]:
        return check([s[:1] + s[2:]])

    return 'NO'


print(check('geeks'))