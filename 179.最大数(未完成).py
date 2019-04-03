class Solution:
    def largestNumber(self, nums):
        ans = ''
        i = 0
        Len = len(nums)
        idx = [j % 10 for j in nums]
        while i < Len:
            Id = idx.index(max(idx))
            ans += str(nums[Id])
            idx.pop(Id)
            i += 1
        #return ans
        temp = {}
        for num in nums:
            temp[num] = 0
            if num > 10:
                num //= 10
            temp[num] = num




x = Solution()
print(x.largestNumber([10, 2]))


print(34 % 10)
