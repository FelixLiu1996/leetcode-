class Solution:
    def numSpecialEquivGroups(self, A):
        ans = set()
        # 只需要比较子串中的奇数字母个数和偶数字母个数是否相等
        for substr in A:
            substr = ''.join((sorted(substr[::2]) + sorted(substr[1::2])))
            # substr = tuple(sorted(substr[::2]) + sorted(substr[1::2]))
            # set不能存数组，需要将其转换成字符串或者tuple
            ans.add(substr)
        return len(ans)




