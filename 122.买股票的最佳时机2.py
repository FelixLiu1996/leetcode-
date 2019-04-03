class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1,len(prices)):
            """后一天比前一天股票价格高，卖出"""
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

