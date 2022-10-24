def conversion():
    n = 'wali yar khan'
    w = ''
    z = 0

    for i in range(0, len(n)):

        if n[i] == " ":
            w += n[i]
            w += n[i + 1].upper()
            z = 1
        else:
            if z == 1:
                z = 0
            else:
                w += n[i]

    return w[0].upper() + w[1: len(w)]

print(conversion())
