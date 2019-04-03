class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # i = 0
        # while i < len(nums):
        #     if nums[i] < target:
        #         i += 1
        #     elif nums[i] >= target:
        #         return i
        #     elif i == len(nums) - 1:
        #         return i + 1
        for i, n in enumerate(nums):
            if target == n:
                return i
            elif n < target:
                continue
            elif target > nums[-1]:
                return len(nums)

