class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                return False
        return True
x = Solution()
print(x.isPowerOfTwo(218))