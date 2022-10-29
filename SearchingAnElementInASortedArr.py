def search():
    nums = [1, 2, 3, 4, 5, 6]
    target = 6
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(search())