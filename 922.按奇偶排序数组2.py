from itertools import chain
class Solution:
    def sortArrayByParityII(self, A):
        ans = [i for i in A if i % 2 == 0]
        #index = 1
        #i = 0
        # while i < len(A):
        #     if A[i] % 2 != 0:
        #         ans.insert(index, A[i])
        #         index += 2
        #         i += 1
        #     else:
        #         i+= 1
        index = 1
        odd = [i for i in A if i % 2 != 0]
        for i in odd:
            ans.insert(index, i)
            index += 2

        return ans

x = Solution()
print(x.sortArrayByParityII([4, 5, 2, 7]))