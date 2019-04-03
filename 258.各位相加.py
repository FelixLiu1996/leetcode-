class Solution:
    def addDigits(self, num: int) -> int:
        # temp = num
        # while temp > 10:
        #     sum = 0
        #     while num > 0:
        #         sum += (num % 10)
        #         num //= 10
        #     temp = num = sum
        # return temp
        if num == 0:
            return num
        return 1 + (num - 1) % 9
x = Solution()
print(x.addDigits(1))