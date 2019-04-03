class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') <= 1 and s.count('LL') <= 2:
            return True
        else:
            return False
