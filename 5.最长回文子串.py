class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划做法
        if not s:
            return ''
        ans = ''
        n = len(s)
        dp = [[0] * n for i in range(n)]  # 用n^2大小的列表记录是否是回文子串
        max_len = -1000
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j <= 1 or dp[i - 1][j + 1]):
                    # or里的两个顺序不能变
                    # 如果dp[i - 1][j + 1] 是回文子串，且s[i] == s[j] 那么dp[i][j]必为回文子串
                    dp[i][j] = 1
                if dp[i][j] and max_len < i - j + 1:
                    ans = s[j: i + 1]
                    max_len = i - j + 1
        return ans

        # 中心拓展算法
        # 将每一个点看成是中心，分为两种，一种为偶数个数，一种为奇数个数
        # 如acca的中心为cc，aca的中心为c，所以总共有2n-1个中心
        # 逐个判断每个作为中心的长度，最后输出最长的回文子串

        # if not s:
        #     return ''
        # self.ans = ''
        # n = len(s)
        # def helper(i, j):
        #     while i >= 0 and j < n and s[i] == s[j]:
        #         i -= 1
        #         j += 1
        #     if len(self.ans) < j - i - 1:
        #         self.ans = s[i + 1: j]
        # for i in range(n):
        # 这里就是对应上面的一个点作为中心,以及第二行是两个点作为中心
        #     helper(i, i)
        #     helper(i, i + 1)
        # return self.ans

        # 暴力法
        # start, end 保证在每一次while循环内的宽度是一样的，然后移动所有的相同长度的子串
        # end - start 的长度由长变短，所以只要出现回文子串，则是最长回文子串
        # for循环只是记录了需要总共循环n次，因为窗口大小总共有n-1, n-2, ... , 0

        # if not s:
        #     return ''
        # ans = ''
        # n = len(s)
        # def is_palindrome(s):
        #     return s == s[::-1]
        # for i in range(n):
        #     start, end = 0, n - i
        #     while end <= n:
        #         sub_string = s[start: end]
        #         if is_palindrome(sub_string):
        #             return sub_string
        #         # 可以看成是一个等长的移动窗口
        #         start += 1
        #         end += 1
