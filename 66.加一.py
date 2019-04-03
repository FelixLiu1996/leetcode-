class Solution:
    def plusOne(self, digits):
        i = len(digits) - 1
        digits[i] += 1
        while i >= 0:
            if i > 0 and digits[i] == 10:
                digits[i] = 0
                digits[i - 1] += 1
            if i == 0 and digits[0] == 10:
                    digits[i] = 0
                    digits.insert(0, 1)
            i -= 1
        return digits
x = Solution()
print(x.plusOne([4, 3, 2, 1]))