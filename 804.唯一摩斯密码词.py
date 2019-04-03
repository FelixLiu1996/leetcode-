class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",\
                 ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",\
                 ".--","-..-","-.--","--.."]
        ans = []
        for word in words:
            word2morse = ''
            for i in word:
                temp = ord(i) - ord('a')
                word2morse += morse[temp]
            if word2morse not in ans:
                ans.append(word2morse)
        return len(ans)