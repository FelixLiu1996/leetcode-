class Solution:
    def lengthOfLIS(self, nums):
        # if not nums:
        #     return 0
        # dp = []
        # for i in range(len(nums)):
        #     dp.append(1)
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # 贪心
        # 让末尾的元素尽可能的小
        d = [] # 存储长度为i的最长子序末尾元素的最小值
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                # 如果 num[i] <= d[-1], 进行二分查找 找到第一个大于num[i]的数，插入
                left, right = 0, len(d) - 1
                loc = right
                while left <= right:
                    mid = (left + right) // 2
                    if d[mid] >= n:
                        loc = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                d[loc] = n
        return len(d)
