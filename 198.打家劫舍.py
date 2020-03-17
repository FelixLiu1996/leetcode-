class Solution:
    def rob(self, nums) -> int:
        # """有可能最后一个位置越过去"""
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        nums.append(0)
        money = [nums[0]]
        money.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            money.append(max(money[i - 2] + nums[i], money[i - 1]))
        return money[-1]
    
x = Solution()
print(x.rob([1,2,3,1]))
