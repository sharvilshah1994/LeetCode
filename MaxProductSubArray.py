import operator


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = {}
    ans = 1
    for _ in nums:
        l[_] = [_]
        ans *= _
    l[ans] = nums
    for _ in range(1, len(nums)):
        ans = nums[_-1]
        for k in nums[_:]:
            ans *= k
            l[ans] = nums[_ - 1: nums.index(k) + 1]
    d = []
    print(l)
    for _ in l:
        d.append(_)
    m = max(d)
    return m

print(maxProduct([-4, -3, -2]))