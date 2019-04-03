class Solution:
    def removeDuplicates(self, nums) -> int:
        Len = len(nums) - 1
        idx1, idx2 = 0, 1
        while idx1 < Len:
            if nums[idx1] == nums[idx2]:
                nums.pop(idx2)
            else:
                idx1 = idx2
                idx2 += 1
        return len(nums)
