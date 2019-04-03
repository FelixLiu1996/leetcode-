class Solution:
    def checkPossibility(self, nums) -> bool:
        len_num = len(nums)
        nums.append(len_num)
        nums.insert(0, 0)
        count = 1
        # for i in range(1, len_num + 1):
        #     if nums[i] > nums[i + 1]:
        #         if nums[i - 1] == nums[i]:
        #             nums[i + 1] = (nums[i] + nums[i + 2]) // 2
        #         else:
        #             nums[i] = (nums[i - 1] + nums[i + 1]) // 2
        #         count -= 1
        #     if count < 0:
        #         return False
        for i in range(1, len_num + 1):
            if nums[i] < nums[i - 1]:
                count -= 1
                if nums[i - 1] > nums[i + 1] or nums[i - 2] > nums[i - 1]:
                    return False
            if count < 0:
                return False
        return True
