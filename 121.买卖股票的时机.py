from sys import maxsize
class Solution:
    def maxProfit(self, prices) -> int:
        """第k个位置的最大利润来自
        前k-1个位置的最大利润与第k个位置与前k-1个位置的最小值 的最大值
        """
        minNum = maxsize
        profit = 0
        for i in range(len(prices)):
            minNum = min(minNum, prices[i])
            profit = max(prices[i] - minNum, profit)
        return profit

x = Solution()
print(x.maxProfit([7,1,5,3,6,4]))


