def distinct():
    n = int(input())
    nums = [int(x) for x in input().split()]

    # nums = [2, 3, 2, 2, 3]
    count = 0

    hash_map = {}

    for i, n in enumerate(nums):
        if n not in hash_map:
            hash_map[n] = i
            count += 1
        # print(hash_map)

    return count 
            
print(distinct())