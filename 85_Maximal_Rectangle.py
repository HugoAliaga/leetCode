from functools import lru_cache


class Solution:
    def maximalRectangle2(self, matrix):
        if not matrix: return 0
        if len(matrix[0])==0: return 0
        ans = 0
        n = len(matrix)
        m = len(matrix[0])

        @lru_cache(maxsize=None)
        def dfs(c1,c2,k,l):
            column = [matrix[x][l] for x in range(c1,k+1)]
            if sum(column)<len(column):
                return 0
            if sum(matrix[k][c2:l+1])<len(matrix[k][c2:l+1]):
                return 0
            a1,a2=0,0
            if k<n-1:
                a1=dfs(c1,c2,k+1,l)
            if l<m-1:
                a2=dfs(c1,c2,k,l+1)
            ans = max((k-c1+1)*(l-c2+1),a1,a2)
            return ans
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=int(matrix[i][j])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==1:
                    ans = max(ans,dfs(i,j,i,j))
        return ans


    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        stack = []
        n = len(matrix)
        m = len(matrix[0])
        height = [0]*(m+1)
        ans=0
        for row in matrix:
            for j in range(m):
                height[j] = height[j] + 1 if row[j]=='1' else 0
            stack = [-1]
            for j in range(m+1):
                while height[stack[-1]]>height[j]:
                    h = height[stack.pop()]
                    w = j - stack[-1] -1
                    ans = max(ans,h*w)
                stack.append(j)
        return ans

tests = []
solutions = []

tests.append([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
solutions.append(6)

tests.append([["0"]])
solutions.append(0)

tests.append([["1"]])
solutions.append(1)

for i in range(len(tests)):
    ans = Solution().maximalRectangle(tests[i])
    print('T',i,'R',ans,solutions[i])