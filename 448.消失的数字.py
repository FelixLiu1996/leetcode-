class Solution:
    def findDisappearedNumbers(self, nums):
        #用列表解析在数据量大的情况下运行超时
        #ans = [i for i in range(1, len(nums) + 1) if i not in nums]
#         temp = [i for i in range(1, len(nums) + 1)]
#         ans = set(temp) - set(nums)
#         ans = list(ans)
#         return ans
# x = Solution()
# print(x.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        ans = []
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
x = Solution()
print(x.findDisappearedNumbers([1, 2, 3, 4, 5, 5, 6, 7]))

