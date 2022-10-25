list = []
def toh(number, start, aux, end):
    global list
    if number == 1:
        list.append(start + ' ' + end)
        # print("Disk 1 move from rod {} to rod {}".format(start, end))
        return 

    toh(number - 1, start, end, aux)
    list.append(start + ' ' + end)
    # print("Disk {} move from rod {} to rod {}".format(number, start, end))
    toh(number - 1, aux, start, end)

    return ''

toh(int(input()), '1', '2', '3')
print(len(list))
for i in list:
    print(i)