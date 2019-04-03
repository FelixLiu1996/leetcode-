class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        temp = nums[0]
        type = 1
        for num in nums:
            if temp != num:
                type += 1
                temp = num
        return type != len(nums)

