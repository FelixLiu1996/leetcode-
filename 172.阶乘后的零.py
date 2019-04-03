class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 0
        count_zero = 0
        while 5 ** i <= n:
            i += 1
        for j in range(1, i):
            count_zero += n // 5 ** j
        return count_zero


x = Solution()
print(x.trailingZeroes(31))