def subset_sum(arr, target):
    n = len(arr) + 1
    w = target + 1
    t = [[0 for i in range(w)] for j in range(n)]
    
    for i in range(n):
        for j in range(w):
            if i == 0 and j != 0:
                t[i][j] = False
            elif j == 0:
                t[i][j] = True

    for i in range(1, n):
        for j in range(1, w):
            if arr[i - 1] <= j:
                t[i][j] = max(t[i - 1][j - arr[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]

    return t[n - 1][w - 1]

print(subset_sum([2, 3, 7, 8, 10], 30))