class Solution:
    def distributeCandies(self, candies) -> int:
        return min(len(list(set(candies))), len(candies) // 2)
x = Solution()
print(x.distributeCandies([1,1,1,1,2,2,2,3,3,3]))