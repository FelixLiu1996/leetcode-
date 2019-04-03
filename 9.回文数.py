import math
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = list(str(x))
        if temp[0] == '-':
            return False
        else:
            for i in range(0, len(temp) // 2):
                if temp[i] != temp[len(temp) - 1 - i]:
                    return False
            return True

x = Solution()
print(x.isPalindrome(-123))
'''
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp = str(x)[::-1]
            if str(x) == temp:
                return True
            else:
                return False
'''
def a(x):
    q = ''
    if x / 1000 >= 1:
        y = int(x / 1000)
        print(y)
        for i in range(0, y):
            q += 'i'
    return q
print(a(1999))