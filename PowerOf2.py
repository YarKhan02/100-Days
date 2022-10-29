def power():
    n = 98
    p = 0
    i = 0

    while p < n:
        p = pow(2, i)
        if p == n:
            return True
        i += 1

    return False

print(power())