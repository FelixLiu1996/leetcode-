class Solution:
    def hIndex(self, citations) -> int:
        if not citations:
            return 0
        citations = sorted(citations)
        ans = len(citations) # ans 记录h指数
        for citation in citations:
            if citation >= ans:
                return ans
            else:
                ans -= 1
        return ans

