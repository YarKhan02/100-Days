def rotate():
    nums = [1, 2, 3, 4, 5]

    for i in range(len(nums)):
        temp = nums[len(nums) - 1]
        print(temp)
        nums[len(nums) - 1] = nums[i]
        nums[i] = temp
        print(nums)

    return nums

print(rotate())