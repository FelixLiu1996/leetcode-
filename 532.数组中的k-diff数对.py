class Solution:
    def findPairs(self, nums, k: int) -> int:
        countPairs = 0
        if k == 0:
            dic = {}
            for num in nums:
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
            for value in dic.values():
                if value > 1:
                    countPairs += 1
            return countPairs
        else:
            # nums = list(set(nums))
            # nums.sort()
            # idx1 = 0
            # idx2 = 1
            # while idx1 < len(nums) and idx2 < len(nums):
            #     if abs(nums[idx1] - nums[idx2]) == k:
            #         idx1 += 1
            #         idx2 = idx1 + 1
            #         countPairs += 1
            #         continue
            #     elif abs(nums[idx1] - nums[idx2]) < k:
            #         idx2 += 1
            #     elif abs(nums[idx1] - nums[idx2]) > k:
            #         idx1 += 1
            #         idx2 = idx1 + 1
            dic = {}
            for num in nums:
                if num in nums:
                    continue
                else:
                    dic[num] = 1
            for item in dic:
                if item - k in dic and k > 0:
                    countPairs += 1
        return countPairs

