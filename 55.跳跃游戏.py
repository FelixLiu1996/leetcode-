# class Solution:
#     def canJump(self, nums) -> bool:
#         # self.stages = len(nums) - 1
#         # def helper(i, nums):
#         #     # 回溯法超出时间限制
#         #     if i >= self.stages:
#         #         return True
#         #     up_stage = min(i + nums[i], self.stages)
#         #     for up in range(i + 1, up_stage + 1):
#         #         if helper(up, nums):
#         #             return True
#         #     return False
#         # return helper(0, nums)
#
#         # 贪心
#         n = len(nums) - 1
#         start = 0
#         end = 0
#         while start <= end and end <= n:
#             end = max(end, nums[start] + start)
#             start += 1
#         return end >= n
#
# x = Solution()
# print(x.canJump([3,2, 1,0,4]))
from urllib import parse
url = parse.quote("北京")
print(url)