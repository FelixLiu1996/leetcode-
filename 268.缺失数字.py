class Solution:
    def missingNumber(self, nums):
        temp = [i for i in range(max(max(nums) + 1, len(nums) + 1))]
        if list(set(temp) - set(nums)) == []:
            return []
        else:
            ans = int(list(set(temp) - set(nums))[0])
            return ans
x = Solution()
print(x.missingNumber([0]))

