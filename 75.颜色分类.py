class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dic = {}
        # dic['0'] = nums.count(0)
        # dic['1'] = nums.count(1)
        # dic['2'] = nums.count(2)
        # nums = []
        # for num in ['0', '1', '2']:
        #     while dic[num] > 0:
        #         nums.append(int(num))
        #         dic[num] -= 1

        # idx0 = 0
        # idx2 = len(nums) - 1
        # for i in range(0, len(nums)):
        #     if idx0 >= idx2:
        #         break
        #     if nums[i] == 0:
        #         nums[idx0], nums[i] = nums[i], nums[idx0]
        #         idx0 += 1
        #     elif nums[i] == 2:
        #         nums[idx2], nums[i] = nums[i], nums[idx2]
        #         idx2 -= 1
        # return nums

        l = 0
        r = len(nums)-1
        #cur=0
        for cur in range(0, len(nums)):
            if l>= r:
                break
            if nums[cur] ==0 :
                nums[l],nums[cur] = nums[cur],nums[l]
                l += 1
                #cur += 1
            elif nums[cur] ==2 :
                nums[r],nums[cur] = nums[cur],nums[r]
                r -= 1
            #else:
                #cur += 1
        return nums

# dic = {'0': 2, '1': 3}
# for num in dic:
#     while dic[num] > 0:
#         print(num)
#         dic[num] -= 1
x = Solution()
print(x.sortColors([2,0,2,1,1,0]))


