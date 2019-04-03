class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        countZero = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp > countZero:
                    countZero = temp
                temp = 0
                continue
        return countZero
