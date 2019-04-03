# import sys
# class Solution:
#     def reverse(self, x: int) -> int:
#         temp = list(str(x))
#         y = []
#         if len(temp) == 1 and temp[0] == '0':
#             return 0
#         else:
#             if temp[len(temp) - 1] == '0':
#                 temp.pop()
#             if temp[0] == '-':
#                 y.append('-')
#                 temp.pop(0)
#             for i in range(0,len(temp)):
#                 y.append(temp.pop())
#             x = ''.join(y)
#             if int(x) > sys.maxsize:
#                 return 0
#             else:
#                 return int(x)
# x = Solution()
# print(x.reverse(0))
# print(sys.maxsize)
a = ['a', 'b']
b = 'b'
print(a.count(b))