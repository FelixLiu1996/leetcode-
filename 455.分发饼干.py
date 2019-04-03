class Solution:
    def findContentChildren(self, g, s) -> int:
        ans = 0
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans

