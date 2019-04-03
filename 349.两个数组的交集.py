class Solution:
    def intersection(self, nums1, nums2):
        num1, num2 = set(nums1), set(nums2)
        ans = num1 & num2
        return list(ans)

x = Solution()
print(x.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))


