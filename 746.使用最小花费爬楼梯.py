class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """p1, p2代表前两个台阶和前一个台阶所花费的体力"""
        """p2也代表跨越最后一个台阶所花费的体力"""
        p1, p2 = 0, 0
        for i in range(2, len(cost) + 1):
            p1, p2 = p2, min(p1 + cost[i - 2], p2 + cost[i - 1])
        return p2