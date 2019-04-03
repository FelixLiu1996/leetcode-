class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        if len(nums[0]) * len(nums) == r * c:
            temp = []
            ans = []
            for num in nums:
                temp += num
            for i in range(r):
                ans += [temp[i * c:(i+1) * c]]
            return ans
        else:
            return nums
x = Solution()
print(x.matrixReshape([[1,2,3],[3, 4,5]],3,2))