class Solution:
    def merge(self, intervals):
        intervals.sort(key = lambda x : x[0])
        if len(intervals) <= 1:
            return intervals
        n = len(intervals)
        i=0
        deleted = 0
        while i <= len(intervals) - 2 and len(intervals)>2:
            if intervals[i][-1]<intervals[i+1][0]:
                i+=1
            else:
                intervals[i][0] = min(intervals[i][0],intervals[i+1][0])
                intervals[i][-1] = max(intervals[i][-1],intervals[i+1][-1])
                deleted +=1
                del intervals[i+1]

        if len(intervals)==2:
            if intervals[0][-1]>=intervals[1][0]:
                intervals[0][0] = min(intervals[0][0],intervals[1][0])
                intervals[0][-1] = max(intervals[0][-1],intervals[1][-1])
                del intervals[1]
        return intervals

tests = []
solutions = []

""" tests.append()
solutions.append() """

tests.append([[1,3],[2,6],[8,10],[15,18]])
solutions.append([[1,6],[8,10],[15,18]])

tests.append([[1,4],[4,5]])
solutions.append([[1,5]])

tests.append([[1,4],[0,4]])
solutions.append([0,4])

tests.append([[1,4],[2,3]])
solutions.append([1,4])

tests.append([[1,4],[0,2],[3,5]])
solutions.append([[0,5]])

tests.append([[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]])
solutions.append([])

for i in range(len(tests)):
    res = Solution().merge(tests[i])
    print('T',i,'R',res,solutions[i])