"""
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        if int(num / 1000) >= 1:
            '''数字大于1000'''
            temp = int(num / 1000)
            for i in range(0, temp):
                ans = ans + 'M'
            num = num - temp * 1000
        if int(num / 500) == 1:
            if int(num / 900) == 1:
                '''判定为900时'''
                ans += 'CM'
                num = num - 900
            else:
                temp = int(num / 100) - 5
                ans += 'D'
                for i in range(0, temp):
                    ans += 'C'
                num = num - temp * 100 - 500
        if int(num / 500) == 0 and int(num / 100) >= 1:
            if int(num / 100) == 4:
                ans += 'CD'
                num = num - 400
            else:
                temp = int(num / 100)
                for i in range(0, temp):
                    ans += 'C'
                num = num - temp * 100
        if int(num / 100) == 0 and int(num / 10) >=1:
            if int(num / 50) == 1:
                """"""
                if int(num / 90) == 1:
                    '''90'''
                    ans += 'XC'
                    num = num - 90
                else:
                    '''60-80'''
                    temp = int(num / 10) - 5
                    ans += 'L'
                    for i in range(0, temp):
                        ans += 'X'
                    num = num - temp * 10 - 50
            else:
                """"""
                if int(num / 40) == 1:
                    """"""
                    ans += 'XL'
                    num = num - 40
                else:
                    """"""
                    temp = int(num / 10)
                    for i in range(0, temp):
                        ans += 'X'
                    num = num - temp * 10
        if int(num / 10) == 0:
            if int(num / 5) == 1:
                if int(num / 9) == 1:
                    ans += 'IX'
                else:
                    temp = num - 5
                    ans += 'V'
                    for i in range(0, temp):
                        ans += 'I'
            else:
                if int(num / 4) == 1:
                    ans += 'IV'
                else:
                    for i in range(0, num):
                        ans += 'I'
        return ans

x = Solution()
print(x.intToRoman(1994))
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        Int = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        Roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ans = ''
        for i in range(0, 13):
            while num >= Int[i]:
                if num >= Int[i]:
                    ans += Roman[i]
                    num -= Int[i]
        return ans
x = Solution()
print(x.intToRoman(1994))





