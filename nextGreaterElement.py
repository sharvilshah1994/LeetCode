def nextGreaterElement(findNums, nums):
    return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]

print(nextGreaterElement([4,1,2], [1,3,4,2]))