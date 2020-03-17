class Solution:
    def minimumTotal(self, triangle):
        height = len(triangle)
        dp = [[] for _ in range(height)]
        for i in range(height):
            dp[i] = [0 for j in range(i + 1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, height):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[-1])

x = Solution()
print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))