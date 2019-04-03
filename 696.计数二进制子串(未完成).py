class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if s == '':
            return 0
        idx1, idx2, ans = 0, 0, 0
        while idx1 < len(s) and idx2 < len(s):
            if s[idx1] == '1':
                while s[idx2] == '1' and idx2 < len(s):
                    idx2 += 1
                    if idx2 == len(s) - 1:
                        break
                if s[idx1 : 2 * idx2 - idx1] == '0' * (idx2 - idx1):
                    ans += 1
                    idx2 = idx1 + 1
            elif s[idx1] == '0':
                while s[idx2] == '0' and idx2 < len(s):
                    idx2 += 1
                    if idx2 == len(s) - 1:
                        break
                if s[idx1 : 2 * idx2 - idx1] == '1' * (idx2 - idx1):
                    ans += 1
                    idx2 = idx1 + 1
            idx1 += 1
        return ans
x = Solution()
print(x.countBinarySubstrings("00110011"))
