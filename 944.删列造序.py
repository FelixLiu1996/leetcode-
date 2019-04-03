# class Solution:
#     def minDeletionSize(self, A) -> int:
        # ans = 0
        # #i表示遍历每个字符串内的每个字符
        # #j表示在不同字符串间的比较
        # for i in range(len(A[0])):
        #     for j in range(1, len(A)):
        #         if A[j - 1][i] > A[j][i]:
        #             ans += 1
        #             break
        # return ans

a = ["cba", "daf", "ghi"]
print(list(zip(*a)))