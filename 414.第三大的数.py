class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) <= 2:
            return nums[0]
        else:
            return nums[2]
x = Solution()
print(x.thirdMax([3, 2, 1]))