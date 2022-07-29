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

    def insert(self, intervals,newInterval):
        intervals.append(newInterval)

        return self.merge(intervals)

tests = []
solutions = []

tests.append([[[1,3],[6,9]],[2,5]])
solutions.append([[1,5],[6,9]])

tests.append([[[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]])
solutions.append([[1,2],[3,10],[12,16]])

for i in range(len(solutions)):
    ans = Solution().insert(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])
        