class Solution:
    def majorityElement(self, nums) -> int:
        Count = 0
        ans = 0
        for num in nums:
            if Count == 0:
                ans = num
            if ans != num:
                Count -= 1
            else:
                Count += 1
        return ans

x= Solution()
print(x.majorityElement([1, 2, 1]))