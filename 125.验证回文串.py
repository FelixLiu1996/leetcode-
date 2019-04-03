class Solution:
    def isPalindrome(self, s: str) -> bool:
        # if s is None:
        #     return True
        # cmpList = list(map(chr, range(ord('a'), ord('z') + 1))) + [str(i) for i in range(0, 10)]
        # s = s.lower()
        # left, right = 0, len(s) - 1
        # #print(left)
        # #print(right)
        # while left < right:
        #     if (s[left] in cmpList) and (s[right] in cmpList) and (s[left] == s[right]):
        #         left += 1
        #         right -= 1
        #     elif s[left] not in cmpList: #and s[right] in cmpList:
        #         left += 1
        #     elif s[right] not in cmpList: #and s[left] not in cmpList:
        #         right -= 1
        #     # elif s[right] not in cmpList: #and s[left] not in cmpList:
        #     #     #left += 1
        #     #     right -= 1
        #     else:
        #         return False
        # return True

        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


x = Solution()
print(x.isPalindrome('0p01'))

# print(list(map(chr, range(ord('a'), ord('z') + 1))))
# a = 'ABC'
# a = a.lower()
# print(a)
