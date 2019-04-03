class Solution:
    def intersect(self, nums1, nums2):
        dic = {}
        ans = []
        for i in nums1:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in nums2:
            if i in dic and dic[i] > 0:
                ans.append(i)
                dic[i] -= 1
        return ans

        # if len(nums1) <= len(nums2):
        #     temp = nums1
        #     nums1 = nums2
        #     nums2 = temp
        # ans = []
        # for i in nums2:
        #     if i in nums1 and ans.count(i) < min(nums1.count(i), nums2.count(i)):
        #         ans.append(i)
        # return ans


x = Solution()
print(x.intersect(nums1 = [1, 2], nums2 = [1, 1]))
