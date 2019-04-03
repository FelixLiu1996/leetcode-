class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        """要么三个正数，要么两个最小的负数得正，再和最大的数相乘"""
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])