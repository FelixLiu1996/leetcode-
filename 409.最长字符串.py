class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        L = []
        for temp in s:
            if s.count(temp) > 1 and s.count(temp) % 2 == 0 and temp not in L:
                ans += s.count(temp)
                L.append(temp)
            elif temp not in L:
                ans += s.count(temp) - 1
                L.append(temp)
        if ans < len(s):
            ans += 1
        return ans
x = Solution()
print(x.longestPalindrome("dccc"))

