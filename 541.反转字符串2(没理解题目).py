class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        if len(s[k:]) > k:
            ans = s[:k][::-1] + s[k:]
        else:
            ans = s[:][::-1] + s[k:][::-1]
        return ans

x = Solution()
print(x.reverseStr(s = "abcdefg", k = 2))
