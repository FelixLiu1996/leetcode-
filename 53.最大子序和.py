class Solution:
    def maxSubArray(self, nums) -> int:
        maxAns = 0
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] > 0 or nums[left] + nums[left - 1] > 0:
                ans += nums[left]
                left += 1
            else:
                maxAns = max(maxAns, ans)
                ans = 0
                left += 1
        return maxAns

x = Solution()
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



