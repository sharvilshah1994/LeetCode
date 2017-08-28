def searchRange(nums, target):
    l = []
    for i in range(len(nums)):
        if len(l) < 2 and target == nums[i]:
            l.append(i)
        elif target == nums[i]:
            l[1] = i
    if len(l) == 0:
        return [-1, -1]
    elif len(l) == 1:
        l.append(l[0])
        return l
    else:
        return l


print(searchRange([1,2,3,3], 3))