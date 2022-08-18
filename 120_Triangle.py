from functools import lru_cache


class Solution:
    def minimumTotal2(self, triangle) -> int:
        lt = len(triangle)-1
        @lru_cache(maxsize=None)
        def dfs(row,idx,path):
            if row < lt:
                op1 = dfs(row+1,idx,path + triangle[row][idx])
                op2 = dfs(row+1,idx+1,path + triangle[row][idx])
                return min(op1,op2)
            else:
                return path + triangle[row][idx]
        return dfs(0,0,0)

    def minimumTotal(self, triangle) -> int:
        while len(triangle) >1:
            for i in range(len(triangle[-1])-1):
                triangle[-2][i] += min(triangle[-1][i],triangle[-1][i+1])
            del triangle[-1]
        return min(triangle[0])

tests = []
solutions = []

tests.append([[2],[3,4],[6,5,7],[4,1,8,3]])
solutions.append(11)

tests.append([[-10]])
solutions.append(-10)

for i in range(len(tests)):
    ans = Solution().minimumTotal(tests[i])
    print('T',i,'R',ans,solutions[i])