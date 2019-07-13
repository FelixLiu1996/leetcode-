class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        Len = len(nums) // 2
        if len(nums) % 2 == 0:
            nums1 = nums[ : Len]
            nums2 = nums[Len: ]
        else:
            nums1 = nums[: Len + 1]
            nums2 = nums[Len + 1:]
        nums[::2] = nums1[::-1]
        nums[1::2] = nums2[::-1]