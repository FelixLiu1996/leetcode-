from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        def compare(a, b):
            if str(b) + str(a) > str(a) + str(b):
                return 1
            else:
                return -1
        ans = sorted(nums, key=cmp_to_key(compare))
        print(ans)
        return ''.join(map(str,ans)).lstrip('0')
x = Solution()
print(x.largestNumber([1,25,5]))