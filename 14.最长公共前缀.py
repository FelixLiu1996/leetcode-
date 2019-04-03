
'''
class Solution:
    def longestCommonPrefix(self, strs):
        List = list(strs)
        minLen = 10000
        str = ''
        for i in range(len(List)):
            if len(List[i]) < minLen:
                minLen = len(List[i])
        for i in range(minLen):
            for j in range(0, len(List) - 1):
                if List[j][i] != List[j + 1][i]:
                    return str
            str += List[0][i]
        return str

x = Solution()
strs = ["","","a"]
print(x.longestCommonPrefix(strs))
'''
'''
class Solution:
    def longestCommonPrefix(self, strs):
        List = list(strs)
        minLen = 10000
        str = ''
        for i in range(len(List)):
            if len(List[i]) < minLen:
                minLen = len(List[i])
        temp = List[0][:minLen]
        for i in temp:
            for j in range(len(List)):
                if List[j] !=
'''
class Solution:
    def longestCommonPrefix(self, strs):
        List = list(strs)
        minLen = 10000
        str = ''
        for i in range(len(List)):
            if len(List[i]) < minLen:
                minLen = len(List[i])
        low = 0
        high = minLen
        while low <= high:
            test = False
            mid = (high + low) // 2
            for i in range(len(List)):
                if List[i][:mid] != List[0][:mid]:
                    test = False
                else:
                    test = True
            if test == False:
                high = mid - 1
            elif test == True:
                low = mid + 1

        return List[0][: mid]
x = Solution()
str = ["dog","racecar","car"]
print(x.longestCommonPrefix(str))