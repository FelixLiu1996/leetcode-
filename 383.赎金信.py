class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        magazine = list(magazine)
        ransomNote = list(ransomNote)
        for letter in magazine:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        for letter in ransomNote:
            if letter in dic and dic[letter] > 0:
                dic[letter] -= 1
            else:
                return False
        return True

x = Solution()
print(x.canConstruct('a', 'b'))
