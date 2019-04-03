class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        """切片的效率太低，时间复杂度高"""
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     if nums[left] == min(nums[left:right + 1]):
        #         left += 1
        #     else:
        #         break
        # while right >= left:
        #     if nums[right] == max(nums[left:right + 1]):
        #         right -= 1
        #     else:
        #         break
        # return right - left + 1
        left, right = 0, len(nums) - 1
        arr = sorted(nums)
        while left < len(nums) and arr[left] == nums[left]:
            left += 1
        while right < len(nums) and arr[right] == nums[right]:
            right -= 1
        return max(right - left + 1, 0)