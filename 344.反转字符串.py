class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        #s = s[::-1]
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



