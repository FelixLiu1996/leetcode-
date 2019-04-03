class Solution:
    def smallestRangeI(self, A, K):
        return max(max(A) - min(A) - 2 * K, 0)


x = Solution()
print(x.smallestRangeI(A = [1,3,6], K = 3))
