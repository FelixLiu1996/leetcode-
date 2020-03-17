class Solution:
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        n_arr = ['' for i in range(numRows)]
        flag = -1
        curr = 0
        for char in s:
            if curr == 0 or curr == numRows - 1:
                flag = -flag
            n_arr[curr] += char
            curr += flag
        ans = ''
        for char in n_arr:
            ans += char
        return ans

x = Solution()
print(x.convert(s = "LEETCODEISHIRING", numRows = 3))