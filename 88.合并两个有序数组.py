class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        idx1, idx2 = 0, 0
        len1 = len(nums1)
        len2 = len(nums2)
        if len(nums2) == 0 or len(nums1) == 0:
            #print(nums1)
            return
        while idx1 < len1 and idx2 < len(nums2):
            if nums2[idx2] <= nums1[idx1]:
                nums1.insert(idx1, nums2[idx2])
                idx1 += 1
                nums2.pop(idx2)
            else:
                idx1 += 1
        nums1 += nums2
        print(nums1)
x = Solution()
x.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)

