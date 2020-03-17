class Solution:
    def myPow(self, x, n):
        ans = 1
        if n == 0:
            return ans
        elif n > 0:
            while n > 0:
                if n % 2 != 0:
                    # 奇数的话 要多乘一个x
                    ans *= x
                x *= x
                n //= 2
            return ans
        else:
            n = abs(n)
            while n > 0:
                if n % 2 != 0:
                    ans *= x
                x *= x
                n //= 2
            return 1 / ans

x = Solution()
print(x.myPow(2.00000, -2))