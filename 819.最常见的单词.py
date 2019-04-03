class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        a = ',.!\'@#$%^&*()\"?:;'
        for i in a:
            paragraph = paragraph.replace(i, ' ')
        para = paragraph.lower().split()
        Count = 0
        ans = ''
        for i in para:
            i = i.strip(',')
            if para.count(i) > Count and i not in banned:
                Count = para.count(i)
                ans = i
        return ans

x = Solution()
print(x.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",\
banned = ["hit"]))
