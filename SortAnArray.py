def insert(arr, temp):
    if((len(arr) - 1) == 0) or (arr[len(arr) - 1] <= temp):
        arr.append(temp)
        return

    val = arr[len(arr) - 1]
    arr.pop(len(arr) - 1)
    insert(arr, temp)
    arr.append(val)

def sorting(arr):
    if(len(arr) - 1) == 0:
        return

    temp = arr[len(arr) - 1]
    arr.pop(len(arr) - 1)
    sorting(arr)
    insert(arr, temp)

arr = [1, 5, 2, 4]

sorting(arr)

print(arr)
