class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        """这样做太慢"""
        # idx1 = 0
        # while idx1 < len(nums):
        #     idx2 = idx1 + min(k, len(nums) - idx1)
        #     if nums[idx1] in nums[idx1: idx2 + 1]:
        #         return True
        #     idx1 += 1
        # return False
        if len(nums) <= 1:
            return False
        dic = {}
        """键存值，值存索引"""
        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k:
                    return True
                dic[nums[i]] = i
        return False
