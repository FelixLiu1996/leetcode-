class Solution:
    def nthUglyNumber(self, n: int) -> int:
        choushu = [1]
        idx2 = 0
        idx3 = 0
        idx5 = 0
        for i in range(n - 1):
            choushu.append(min(choushu[idx2] * 2, choushu[idx3] * 3, choushu[idx5] * 5))
            if choushu[-1] == choushu[idx2] * 2:
                idx2 += 1
            if choushu[-1] == choushu[idx3] * 3:
                idx3 += 1
            if choushu[-1] == choushu[idx5] * 5:
                idx5 += 1
        return choushu[-1]




x = Solution()
print(x.nthUglyNumber(5))
