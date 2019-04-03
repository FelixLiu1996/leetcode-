class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #   算法超时
        # if num <= 2:
        #     return False
        # factors = [1]
        # for i in range(2, num // 2 + 1):
        #     if num % i == 0:
        #         factors.append(i)
        #         factors.append(num / i)
        # factors = list(set(factors))
        # return sum(factors) == num

        if num < 2:
            return False
        #factors = [1]
        ans = 1
        for i in range(2, int(num ** 0.5) + 1):
            #int(num ** 0.5) + 1 保证不会重复计算因子两次
            if num % i == 0:
                ans += i + num / i
                # factors.append(i)
                # factors.append(num / i)
        #factors = list(set(factors))
        #return sum(factors) == num
        return ans == num

x = Solution()
print(x.checkPerfectNumber(28))
