class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Len = len(s)
        if Len == 0:
            return 0
        while s[Len -1] == ' ' and Len > 0:
            Len -= 1
        if Len == 0:
            return 0
        else:
            i = Len - 1
            ans = 0
            while i >= 0:
                if s[i] != ' ':
                    ans += 1
                    i -= 1
                else:
                    break
            return ans

x = Solution()
print(x.lengthOfLastWord(""))

