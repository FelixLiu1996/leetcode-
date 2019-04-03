class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] == word[0].upper():
            if word[1:] == word[1:].upper():
                return True
            elif word[1:] == word[1:].lower():
                return True
            else:
                return False
        elif word == word.upper():
            return True
        elif word == word.lower():
            return True
        else:
            return False
