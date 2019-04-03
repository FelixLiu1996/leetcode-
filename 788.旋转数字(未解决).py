class Solution:
    def rotatedDigits(self, N: int) -> int:
        def change(a):
            ans = 0
            indice = 0
            while a > 0:
                temp = a % 10
                if temp in [0, 1, 2, 5, 6, 8, 9]:
                    ans = ans + temp*(10**indice)
                    a //= 10
                    indice += 1
                else:
                    return False
            return ans != a
        num = 0
        for i in range(N + 1):
            if change(i):
                num += 1
        return num
x = Solution()
print(x.rotatedDigits(10))
