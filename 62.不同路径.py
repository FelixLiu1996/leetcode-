class Solution:
    # 排列组合 只要选择m x n 矩阵中 在剩下的m-1 与n - 1 的数中选择n-1个向下走
    # def uniquePaths(self, m, n):
    #     return self.combination(m + n - 2, n - 1)
    #
    # def combination(self, n, x):
    #     upper, down = 1, 1
    #     for num in range(n, n - x, -1):
    #         upper *= num
    #     for num in range(x, 0, -1):
    #         down *= num
    #     return upper // down

    # 动态规划
    def uniquePaths(self, m, n):
        dp = [[0 for j in range(m)] for i in range(n)]
        dp[0] = [1 for j in range(m)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

x = Solution()
print(x.uniquePaths(7, 3))

