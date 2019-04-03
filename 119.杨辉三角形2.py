'''
import math
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        else:
            ans = [1]
            for i in range(1, rowIndex):
                ans.append(int(math.factorial(rowIndex) / (math.factorial(i) * math.factorial(rowIndex - i))))
            ans.append(1)
        return ans

x = Solution()
print(x.getRow(3))
'''
class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        else:
            ans = []
            i = j = 1
            h = rowIndex
            while i < rowIndex:
               ans.append(h // j)
               h *= rowIndex - i
               j *= i + 1
               i += 1
            ans.append(1)
            ans.insert(0, 1)
        return ans

x = Solution()
print(x.getRow(4))