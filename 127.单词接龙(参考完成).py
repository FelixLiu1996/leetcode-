from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # 参考 https://blog.csdn.net/fuxuemingzhu/article/details/82903681
        wordset = list(set(wordList))
        bfs = deque()
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in [chr(j) for j in range(ord('a'), ord('z') + 1)]:
                    newWord = word[ : i] + c + word[i + 1: ]
                    if newWord in wordset and newWord != word:
                        wordset.remove(newWord)
                        bfs.append((newWord, length + 1))
        return 0

#  参考另外的双端搜索
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordSet, beginSet, endSet, step = set(wordList), set([beginWord]), set([endWord]), 1
#         if endWord not in wordList:
#             return 0
#         while beginSet:
#             tmpSet, step = set(), step+1
#             for word in beginSet:  # 去掉重复的
#                 if word in wordSet:
#                     wordSet.remove(word)
#             for word in beginSet:
#                 for i in range(len(word)):
#                     tmp = list(word)
#                     for c in list(map(chr, range(ord('a'), ord('z') + 1))):
#                         tmp[i] = c  # 将tmp某一位替换
#                         str_tmp = ''.join(tmp)
#                         if str_tmp in endSet:
#                             return step
#                         if str_tmp in wordSet:
#                             tmpSet.add(str_tmp)
#             if len(tmpSet) > len(endSet):  # 把小set放前面检索的少
#                 beginSet, endSet = endSet, tmpSet
#             else:
#                 beginSet = tmpSet
#         return 0