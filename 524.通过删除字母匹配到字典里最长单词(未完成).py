# class Solution:
#     def findLongestWord(self, s: str, d) -> str:
          #这样不行 因为要保证字典序最小 且不能破坏原字符串的字母顺序
#         # s = list(s)
#         # dic = {}
#         # ans = ''
#         # for i in s:
#         #     if i in dic:
#         #         dic[i] += 1
#         #     else:
#         #         dic[i] = 1
#         # for i in d:
#         #     temp = list(i)
#         #     flag = 1
#         #     for j in temp:
#         #         if j not in dic or temp.count(j) > dic[j]:
#         #             flag = 0
#         #             break
#         #     if flag == 1:
#         #         if len(temp) > len(ans):
#         #             ans = temp
#         #         if len(temp) == len(ans) and temp < ans:
#         #             ans = temp
#         # return ''.join(ans)