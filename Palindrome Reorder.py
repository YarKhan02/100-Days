c = input()
ls = sorted(list(set(c)))
y = ''
half = ''
m = ''
x = 0
     
for i in ls:
    n = c.count(i)
    if n % 2 == 0:
        half += i*(n//2)
    elif x == 1:
        half = 0
        print('NO SOLUTION')
        break
    else:
        x = 1
        m = i
        half += i*((n - 1) // 2)
if half != 0:
    print(half + m + half[::-1])
