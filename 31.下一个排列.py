class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先找出最大的索引k，满足nums[k] < nums[k + 1], 如果不存在，翻转整个数组
        # 再找出另一个最大索引l，满足nums[l] > nums[k]
        # 交换nums[l]与nums[k]
        # 最后翻转nums[k + 1: ]

        n = len(nums)
        k = -1
        l = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break
        if k == -1:
            nums[:] = nums[::-1]
            # print(nums)
            return
        for i in range(n - 1, -1, -1):
            if nums[i] > nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1: ] = nums[n - 1:k:-1]
