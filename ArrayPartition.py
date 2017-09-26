def ArrayPartition(nums):
    if len(nums) < 3:
        return min(nums)
    nums.sort()
    ans = 0
    temp = []
    for _ in nums:
        temp.append(_)
        if len(temp) == 2:
            ans += min(temp)
            temp = []
    return ans

print(ArrayPartition([7,3,1,0,0,6]))