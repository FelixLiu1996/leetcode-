class Solution:
    def firstUniqChar(self, s: str) -> int:
        #此方法太慢
        # ans = -1
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         #print(s.count(s[i]))
        #         ans = s.index(s[i])
        #         break
        #     else:
        #         continue
        # return ans
        lst = list(set(s))
        lst.sort(key=s.index)
        for i in lst:
            a = s.count(i)
            if a == 1:
                return s.index(i)
        return -1

x = Solution()
print(x.firstUniqChar('loveleetcode'))
#print('loveleetcode'.count('l'))
#print('loveleetcode'.index(''))