# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
class Solution:
    def merge(self, intervals):
        intervals = [[x.start, x.end] for x in intervals]
        intervals.sort(key=lambda x: (x[0], x[1]))
        #print(intervals)
        i = 1
        #Len = len(intervals)
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i][0], intervals[i][1] = intervals[i - 1][0], max(intervals[i][1], intervals[i - 1][1])
                intervals.pop(i - 1)
                i += 1
            else:
                i += 1
        return intervals
#
# x = Solution()
# a = Interval()
# p
#print(x.merge(list(a)))

a = [1,2,3]
a.remove(1)
print(a)