class Solution:
    def pancakeSort(self, A):
        ans = []
        Len = len(A)
        while Len > 0:
            idx = A.index(max(A[:Len]))
            a1 = A[:idx + 1]
            a2 = A[idx + 1:]
            A = a1[:: -1] + a2[::]
            ans.append(idx + 1)
            a1 = A[:Len]
            a2 = A[Len:len(A)]
            A = a1[::-1] + a2[::]
            #print(A)

            ans.append(Len)
            Len -= 1
        return ans



#a = [1, 3, 4, 2]
# idx = a.index(max(a))
# a1 = a[:idx + 1]
# a2 = a[idx+1:]
# a = a1[::-1] + a2[::]

#print(a[::-1])
x = Solution()
print(x.pancakeSort([3,2,4,1]))
