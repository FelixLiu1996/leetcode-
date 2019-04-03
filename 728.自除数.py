class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ans = []
        for num in range(left, right + 1):
            temp = num
            while temp > 0:
                if temp % 10 == 0:
                    break
                if temp > 10:
                    if (num % (temp % 10)) == 0:
                        temp //= 10
                    else:
                        break
                else:
                    if num % temp == 0:
                        ans.append(num)
                        break
                    else:
                        break
        return ans

x = Solution()
print(x.selfDividingNumbers(1, 22))

