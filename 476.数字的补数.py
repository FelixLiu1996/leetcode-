class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        num = list(num)
        for i in range(len(num)):
            if num[i] == '1':
                num[i] = '0'

            else:
                num[i] = '1'
        num = ''.join(num)
        return int(num, 2)

x = Solution()
print(x.findComplement(5))