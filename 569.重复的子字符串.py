class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        Len = len(s)
        if Len == 1:
            return False
        # if Len % 2 != 0:
        #     """奇数情况"""
        #     if s.count(s[0]) != Len:
        #         return False
        #     else:
        #         return True
        # else:
        #     i = 0
        #     while i < Len - 1:
        #         if (s[0:i + 1] * (Len // (i + 1))) == s:
        #             return True
        #         else:
        #             i += 1
        # return False
        i = 0
        while i < Len - 1:
            if (s[0:i + 1] * (Len // (i + 1))) == s:
                return True
            else:
                i += 1
        return False

x = Solution()
print(x.repeatedSubstringPattern("babbabbabbabbab"))
