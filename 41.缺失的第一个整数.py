class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        i = 1
        while i < max(nums) or i <= len(nums):
            if i not in nums:
                break
            i += 1
        return i




        # for i in range(1, max(nums)):
        #     if i not in nums:
        #         return i
x = Solution()
print(x.firstMissingPositive([1]))
