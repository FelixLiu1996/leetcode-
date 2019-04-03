class Solution:
    def mySqrt(self, x: int) -> int:
        right = x
        while right * right > x:
            right = (right + x / right) // 2
        return int(right)

x = Solution()
print(x.mySqrt(9))