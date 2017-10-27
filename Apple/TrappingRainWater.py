class Solution(object):
    def trap_water(self, arr):
        n = len(arr)
        l, r = 0, n - 1
        m_height, water = 0, 0
        while l < r:
            while l < r and arr[l] <= m_height:
                water += m_height - arr[l]
                l += 1
            while l < r and arr[r] <= m_height:
                water += m_height - arr[r]
                r -= 1
            m_height = min(arr[l], arr[r])
        return water


if __name__ == "__main__":
    s = Solution()
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap_water(h))
