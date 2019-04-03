class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums[:]:
            if num == 0:
                nums.remove(num)
                nums.append(0)
        print(nums)
x = Solution()
x.moveZeroes([0, 0, 1])
