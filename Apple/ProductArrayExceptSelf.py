class Solution():
    def get_product_except_self(self, nums):
        p = 1
        n = len(nums)
        answer = []
        for i in range(0, n):
            answer.append(p)
            p *= nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= p
            p *= nums[i]
        return answer


ans = Solution()
print(ans.get_product_except_self([1, 2, 3, 4]))
