class Solution:
    def countSegments(self, s: str) -> int:
        # if s == '':
        #     return 0
        # ans = 0
        # for i in range(1, len(s)):
        #     if s[i] in ' ,.!:;\"' and s[i-1] not in ' ,.!:;\"':
        #         ans += 1
        # if s[-1] not in ' ,.!:;\"':
        #     ans += 1
        # return ans
        return len(s.split())



