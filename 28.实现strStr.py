class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None:
            return 0
        else:
            if needle in haystack:
                print(haystack.index(needle))
            else:
                return -1

