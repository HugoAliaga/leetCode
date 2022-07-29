class Solution:
    def uniquePathsWithObstacles(self, grid) -> int:
        def dfs(grid,memo):
            if grid[0][0]==1 or grid[-1][-1]==1: return 0
            if len(grid)==1:
                if 1 in grid[0]: return 0
                return 1
            if len(grid[0])==1:
                for i in grid:
                    if i[0] ==1: return 0
                return 1

            grid_text = ''
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    grid_text += str(grid[i][j])
                grid_text += ','
            if grid_text in memo: return memo[grid_text]

            total = 0
            if grid[0][1]!=1:
                grid_right = []
                for i in grid:
                    grid_right.append(i[1:])
                total += dfs(grid_right,memo)
            if grid[1][0]!=1:
                total += dfs(grid[1:],memo)
            memo[grid_text] = total
            return total
        memo = {}
        return dfs(grid,memo)
tests= []
solutions = []

tests.append([[0,0,0],[0,1,0],[0,0,0]])
solutions.append(2)

tests.append([[0,1],[0,0]])
solutions.append(1)

tests.append([[0]])
solutions.append(1)

tests.append([[1]])
solutions.append(0)

tests.append([[0,0],[1,1],[0,0]])
solutions.append(0)

tests.append([[1,0],[0,0]])
solutions.append(0)

for i in range(len(tests)):
    ans = Solution().uniquePathsWithObstacles(tests[i])
    print('T',i,'R',ans,solutions[i])