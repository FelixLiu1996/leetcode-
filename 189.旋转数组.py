class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[: len(nums) - k]
        print(nums)
x = Solution()
x.rotate([1,2,3,4,5,6,7], k=3)