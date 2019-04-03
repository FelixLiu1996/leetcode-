class NumArray:

    def __init__(self, nums):
        self.ans = nums
        for i in range(1, len(nums)):
            self.ans[i] += self.ans[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.ans[j]
        else:
            return self.ans[j] - self.ans[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)