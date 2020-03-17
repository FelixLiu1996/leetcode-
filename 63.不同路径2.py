class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        # 特殊
        if obstacleGrid[0][0] == 1:
            return 0
        # 边界条件
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                dp[0][j] = 1
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
x = Solution()
print(x.uniquePathsWithObstacles([[1,0],[0,0]]))