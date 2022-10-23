def vowel(v):
    vowels = 'aeiou'
    x = ''
    y = ''
    j = 0

    for i in v:
        if i in vowels:
            x = str(i) + x
            # print(x, end = '')

    # print('x = ', x)

    for i in v:
        if i in vowels:
            y = y + x[j]
            j += 1
        else:
            y = y + i
        
        # print('After condition', y)

    # print('')

    return y

print(vowel('hello'))