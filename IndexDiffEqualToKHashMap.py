def containsCloseNums(nums, k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            if (i - dic[nums[i]]) <= k:
                return True
            else:
                dic[nums[i]] = i
        else:
            dic[nums[i]] = i
    return False


print(containsCloseNums(nums=[0, 1, 2, 3, 5, 2], k=3))
