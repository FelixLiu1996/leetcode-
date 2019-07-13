class Solution:
    def searchRange(self, nums, target):
        # 题目要求时间复杂度O(logn)，所以使用二分查找
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums)
        ans = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left, right = mid, mid
                while left > 0 and nums[left] == nums[left - 1]:
                    left -= 1
                while right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right += 1
                ans[0], ans[1] = left, right
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return ans

