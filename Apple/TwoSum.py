class Solution(object):
    def two_sum(self, nums, target):
        mapping = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] in mapping:
                return [mapping[nums[i]], i]
            else:
                mapping[target - nums[i]] = i


ans = Solution()
print(ans.two_sum(nums=[2, 3, 4], target=6))