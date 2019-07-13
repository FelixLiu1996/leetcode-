class Solution:
    def findAnagrams(self, s: str, p: str):
        # 暴力法 超时
        # n = len(s)
        # m = len(p)
        # dic = {}
        # for i in p:
        #     if i not in dic:
        #         dic[i] = 1
        #     else:
        #         dic[i] += 1
        # ans = []
        # for i in range(n):
        #     if i + m < n:
        #         temp = s[i: i + m]
        #         flag = True
        #         for j in set(temp):
        #             if j not in dic or temp.count(j) != dic[j]:
        #                 flag = False
        #         if flag:
        #             ans.append(i)
        #     else:
        #         break
        # return ans

        # 滑窗法
        n = len(s)
        m = len(p)
        ans = []
        dic = {}
        for i in p:
            dic[i] = dic.get(i, 0) + 1
        # 这个与用get方法等效
        # for i in p:
        #     if i not in p:
        #         dic[i] = 1
        #     else:
        #         dic[i] += 1
        temp = s[: m]
        dic_compare = {}
        for i in temp:
            dic_compare[i] = dic_compare.get(i, 0) + 1
        if dic == dic_compare:
            ans.append(0)
        # i 是要去掉的位置，所以新开头的位置是i+1
        # 一定注意 如果一个元素减到0，要把它去掉，不然会影响结果
        for i in range(n - m):
            dic_compare[s[i]] -= 1
            dic_compare[s[i + m]] = dic_compare.get(s[i + m], 0) + 1
            if dic_compare[s[i]] == 0:
                dic_compare.pop(s[i])
            if dic == dic_compare:
                ans.append(i + 1)
        return ans







