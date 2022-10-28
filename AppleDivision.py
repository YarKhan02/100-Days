def minimum(nums, curr, tsum, i):
    if i == 0:
        return abs((tsum - curr) - curr)

    return min(minimum(nums, curr + nums[i], tsum, i - 1), minimum(nums, curr, tsum, i - 1))


def main():
    n = int(input()) 
    nums = [int(x) for x in input().split()]
    tsum = sum(nums)
    
    result = minimum(nums, 0, tsum, n - 1)

    print(result)

    return ''

print(main())
