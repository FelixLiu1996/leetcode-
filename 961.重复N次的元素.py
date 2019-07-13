class Solution:
    def repeatedNTimes(self, A) -> int:
        # dic = {}
        # for i in range(len(A)):
        #     if A[i] in dic:
        #         dic[A[i]] += 1
        #     else:
        #         dic[A[i]] = 1
        # # for i in range(len(A)):
        # #     dic[A[i]] = dic.get(A[i], 0) + 1
        # ans = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # return ans[0][0]
        N = len(A) // 2
        for i in range(len(A)):
            if A.count(A[i]) == N:
                return A[i]
x = Solution()
print(x.repeatedNTimes([1,2,3,3]))