class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        else:
            ans = [[1]]
            for i in range(1, numRows + 1):
                ans.append([(0 if j == 0 else ans[i - 1][j - 1]) + (0 if j == i else ans[i - 1][j]) for j in range(i + 1)])
            return ans[numRows]

x = Solution()
print(x.generate(3))