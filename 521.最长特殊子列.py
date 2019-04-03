class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        #想错了
        # if len(a) < len(b):
        #     a, b = b, a
        # idx1, idx2 = 0, 0
        # ans = 0
        # while idx2 < len(b) and idx1 < len(a):
        #     if a[idx1] == b[idx2]:
        #         idx1 += 1
        #         idx2 += 1
        #     else:
        #         ans += 1
        #         idx1 += 1
        # if ans == 0:
        #     return -1
        # ans += len(a) - idx1
        # return ans
        """两字符串相同返回-1，不相同返回长的那一个的长度"""
        if a == b:
            return -1
        else:
            return max(len(a), len(b))


x = Solution()
print(x.findLUSlength("aefawfawfawfaw"\
,"aefawfeawfwafwaef"))