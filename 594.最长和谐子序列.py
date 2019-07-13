class Solution:
    def findLHS(self, nums) -> int:
        dic = {}
        ans = 0
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        dic = sorted(dic.items(), key=lambda x: x[0])
        for key in dic:
            if dic[key - 1] in dic:
                ans = max(ans, dic[key - 1] + dic[key])
        return ans
