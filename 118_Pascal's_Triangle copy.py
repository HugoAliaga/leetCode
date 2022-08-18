class Solution:
    def generate(self, numRows: int):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        ans = [[1],[1,1]]
        i = 2
        while i < numRows:
            ans.append([1])
            for j in range(len(ans[i-1])-2):
                ans[i].append(ans[i-1][j]+ans[i-1][j+1])
            ans[i].append(ans[i-1][-2]+1)
            ans[i].append(1)
            i+=1
        return ans

tests = []
solutions = []

tests.append(1)
solutions.append([[1]])

tests.append(5)
solutions.append([[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

for i in range(len(tests)):
    ans = Solution().generate(tests[i])
    print('T',i,'R',ans,solutions[i])