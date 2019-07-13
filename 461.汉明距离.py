class Solution:
    def hammingDistance(self, x, y):
        # 对x，y取异或
        # 然后计算异或之后的1的个数
        res = x ^ y
        ans = 0
        while res > 0:
            ans += (res % 2)
            res //= 2
        return ans
        # 一句话做法
        # return bin(x ^ y).count('1')
x = Solution()
print(x.hammingDistance(1, 4))
