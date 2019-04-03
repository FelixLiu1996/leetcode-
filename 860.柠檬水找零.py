class Solution:
    def lemonadeChange(self, bills) -> bool:
        change = {5:0, 10: 0, 15: 0}
        for bill in bills:
            if bill == 5:
                change[bill] += 1
            elif bill == 10:
                if change[bill - 5] > 0:
                    change[bill - 5] -= 1
                    change[bill] += 1
                else:
                    return False
            elif bill == 20:
                if change[bill - 10] > 0 and change[bill - 15] > 0:
                    change[bill - 10] -= 1
                    change[bill - 15] -= 1
                elif change[bill - 15] >= 3:
                    change[bill - 15] -= 3
                else:
                    return False
        return True
x = Solution()
print(x.lemonadeChange([10,10]))
