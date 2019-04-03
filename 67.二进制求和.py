class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return str(bin(a + b)[2:])
x = Solution()
print(x.addBinary(a = "11", b = "1"))