class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n > 0:
            ans.append(chr((n - 1) % 26 + 65))
            n -= 1
            n //= 26

        ans[:] = ans[::-1]
        ans = ''.join(ans)
        return ans
x = Solution()
print(x.convertToTitle(2))
