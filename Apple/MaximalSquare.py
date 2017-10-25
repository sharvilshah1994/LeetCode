class Solution(object):
    def maximal_square(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = []
        for k in matrix:
            l = []
            for j in k:
                if j == '1':
                    l.append(1)
                else:
                    l.append(0)
            dp.append(l)
        for k in range(1, m):
            for j in range(1, n):
                if matrix[k][j] == '1':
                    dp[k][j] = min(dp[k - 1][j], dp[k][j - 1], dp[j - 1][k - 1]) + 1
                else:
                    dp[k][j] = 0
        m = max([max(i) for i in dp])
        return m ** 2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximal_square(matrix))
