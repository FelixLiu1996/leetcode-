class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            if num < 0:
                return False
            while num >= 1:
                if num % 2 == 0:
                    num /= 2
                elif num % 3 == 0:
                    num /= 3
                elif num % 5 == 0:
                    num /= 5
                else:
                    break
            if num > 1:
                return False
            else:
                return True
x = Solution()
print(x.isUgly(-8))


