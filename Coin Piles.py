# a = 2x + y
# b = x + 2y


n = int(input())

while n != 0:
    a, b = [int(_) for _ in input().split()]

    x = ((2*a) - b) % 3
    x1 = ((2*a) - b)
    y = ((2*b) - a) % 3
    y1 = ((2*b) - a)

    if (x == 0) and (x1 >= 0) and (y == 0) and (y1 >= 0):
        print('YES')
    else:
        print('NO')

    n -= 1