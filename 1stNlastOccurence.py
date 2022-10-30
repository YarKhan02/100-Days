def search():
    nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    k = 5

    left = occur(nums, k, True)
    right = occur(nums, k, False)

    return left, right

def occur(nums, k, leftBias):
    i = -1
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < k:
            low = mid + 1
        elif nums[mid] > k:
            high = mid - 1
        else:
            i = mid
            if leftBias:
                high = mid - 1
            else:
                low = mid + 1

    return i


print(search())

