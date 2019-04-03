# class Solution:
#     def calPoints(self, ops):
#         score = [0] * len(ops)
#         score[0] = int(ops[0])
#         for i in range(1, len(ops)):
#             if ops[i] == '+':
#                 score[i] = score[i - 1] + score[i - 2]
#             elif ops[i] == 'D':
#                 score[i] = score[i - 1] * 2
#             elif ops[i] == 'C':
#                 score[i] = score[i - 1] - int(ops[i - 1])
#             else:
#                 score[i] = score[i - 1] + int(ops[i])
#         return score

# class Solution:
#     def calPoints(self, ops):
#         scores = []
#         for i in range(0, len(ops)):
#             if ops[i] == '+':
#                 score = scores[i] + scores[i - 1]
#                 scores.append(score)
#             elif ops[i] == 'D':
#                 score = scores[i - 1] * 2
#                 scores.append(score)
#             elif ops[i] == 'C':
#                 scores.pop()
#             else:
#                 scores.append(int(ops[i]))
#         return sum(scores)

class Solution:
    def calPoints(self, ops):
        scores = []
        for i in ops:
            length = len(scores)

            if i == 'C':
                scores.pop(length - 1)
            elif i == 'D':
                score = scores[length - 1] * 2
                scores.append(score)
            elif i == '+':
                score = scores[length - 2] + scores[length - 1]
                scores.append(score)
            else:
                scores.append(int(i))
        return sum(scores)


