class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True  # 空字符可以被分割
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if dp[i] and (s[i: j] in wordDict):
                    dp[j] = True
                    # break
        return dp[-1]

x = Solution()
print(x.wordBreak("aaaaaaa",["aaaa","aaa"]))