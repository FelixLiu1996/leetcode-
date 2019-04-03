class Solution:
    def arrayPairSum(self, nums) -> int:
        # N = len(nums) // 2
        # i = 0
        # ans = 0
        # nums.sort()
        # while i < N:
        #     ans += nums[i * 2]
        #     i += 1
        #return ans
        nums.sort()
        return sum(nums[::2])