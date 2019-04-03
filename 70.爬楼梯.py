from math import sqrt
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            temp = 1
            i = 2
            ans = 2
            while i < n:
                temp, ans = ans, temp + ans
                i += 1
        return ans

        # fibs = [0, 1]
        # i = 2
        # while i <= n + 1:
        #     fibs.append(fibs[i - 1] + fibs[i - 2])
        #     i += 1
        # return fibs[-1]
        #"""递归运行太慢"""
        #"""本质是Fibonaci数列"""
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # else:
        #     return (self.climbStairs(n - 1) + self.climbStairs(n - 2))
x = Solution()
print(x.climbStairs(4))
