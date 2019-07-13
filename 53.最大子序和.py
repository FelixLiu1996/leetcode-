class Solution:
    def maxSubArray(self, nums) -> int:
        # maxAns = 0
        # ans = 0
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     if nums[left] > 0 or nums[left] + nums[left - 1] > 0:
        #         ans += nums[left]
        #         left += 1
        #     else:
        #         maxAns = max(maxAns, ans)
        #         ans = 0
        #         left += 1
        # return maxAns

        # DP
        # 如果加上当前位置的元素为负数，那么说明对后面的结果是不利的，也就是不可行的
        # 所以重新从当前位置的下一个开始计算
        ans = nums[0]
        temp = 0
        for i in range(len(nums)):
            if temp > 0:
                temp = temp + nums[i]
            else:
                temp = nums[i]
            if temp > ans:
                ans = temp
        return ans


x = Solution()
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



