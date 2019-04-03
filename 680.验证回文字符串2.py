class Solution:
    def validPalindrome(self, s: str):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            left, right = s[i + 1: j + 1], s[i : j]
            return (left == left[:: -1]) or (right == right[:: -1])
        return True

x = Solution()
print(x.validPalindrome('abca'))
