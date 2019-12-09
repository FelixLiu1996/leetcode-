
class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #ans = []
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             ans = [i, j]
        #             return ans

        # 两遍hash表
        # hashTable = {}
        # for i in range(len(nums)):
        #     hashTable[nums[i]] = i
        # for i in range(len(nums)):
        #     temp = target - nums[i]
        #     if temp in hashTable.keys() and i != hashTable.get(temp):
        #         return [i, hashTable[temp]]

        # 一遍hash表
        hashtable = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashtable.keys():
                return [i, hashtable[temp]]
            hashtable[nums[i]] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))