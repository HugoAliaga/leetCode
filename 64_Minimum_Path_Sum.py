class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid)-1,len(grid[0])-1
        def dfs(r,c,memo):
            if (r,c) in memo: return memo[(r,c)]
            if r == m and c == n: return grid[r][c]
            total = 0
            if r<m and c<n:
                total = grid[r][c] + min(dfs(r+1,c,memo),dfs(r,c+1,memo))
                memo[(r,c)]=total
                return total
            if r<m:
                total = grid[r][c] + dfs(r+1,c,memo)
            if c<n:
                total = grid[r][c] + dfs(r,c+1,memo)
            memo[(r,c)] = total
            return total
        memo = {}
        return dfs(0,0,memo)
tests= []
solutions = []

tests.append([[1,2,3],[4,5,6]])
solutions.append(12)

tests.append([[1,3,1],[1,5,1],[4,2,1]])
solutions.append(7)

for i in range(len(tests)):
    ans = Solution().minPathSum(tests[i])
    print('T',i,'R',ans,solutions[i])