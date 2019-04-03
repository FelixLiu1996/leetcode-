
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(int(c ** 0.5) + 1):
            temp = c - i ** 2
            if temp ** 0.5 == int(temp ** 0.5):
                return True
        return False
x = Solution()
print(x.judgeSquareSum(5))

