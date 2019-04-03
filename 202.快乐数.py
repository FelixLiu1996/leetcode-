class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        while n > 0:
            sum += (n % 10) ** 2
            n //= 10
        if sum == 1:
            return True
        elif sum in [4, 16, 37, 58, 89, 145, 42, 20]:
            return False
        else:
            return self.isHappy(sum)

x = Solution()
print(x.isHappy(19))