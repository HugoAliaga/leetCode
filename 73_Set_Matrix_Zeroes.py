class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return None
        n_rows = len(matrix)
        n_columns = len(matrix[0])
        # Get the positions that are 0
        stack = []
        for i in range(n_rows):
            for j in range(n_columns):
                if matrix[i][j]==0:
                    stack.append([i,j])
        visited = []
        while stack:
            for i in range(n_rows):
                matrix[i][stack[0][1]]=0
            for j in range(n_columns):
                matrix[stack[0][0]][j]=0  
            stack.pop(0) 
        return matrix

tests = []
solutions = []

tests.append([[1,1,1],[1,0,1],[1,1,1]])
solutions.append([[1,0,1],[0,0,0],[1,0,1]])

tests.append([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
solutions.append([[0,0,0,0],[0,4,5,0],[0,3,1,0]])

for i in range(len(tests)):
    ans = Solution().setZeroes(tests[i])
    print('T',i,'R',ans,solutions[i])