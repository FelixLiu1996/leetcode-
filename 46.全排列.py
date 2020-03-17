class Solution:
    def permute(self, nums):
        ans = []
        self.help_fun(nums, ans, [])
        return ans

    def help_fun(self, nums, ans, ans_each):
        if not nums:
            ans.append(ans_each)
        else:
            for i in range(len(nums)):
                self.help_fun(nums[: i] + nums[i + 1: ], ans, ans_each + [nums[i]])
