class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                ans -= dic[s[i]]
            else:
                ans += dic[s[i]]
        return ans
s = Solution()
print(s.romanToInt('MCMXCIV'))

