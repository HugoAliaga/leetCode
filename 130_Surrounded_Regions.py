class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return []

        m = len(board)
        n = len(board[0])
        def check_adjacents(i,j):
            if extra_board[i][j]=="OO":
                return
            if extra_board[i][j]=="O":
                extra_board[i][j]="OO"
                if i>0:
                    check_adjacents(i-1,j)
                if i<m-1:
                    check_adjacents(i+1,j)
                if j>0:
                    check_adjacents(i,j-1)
                if j<n-1:
                    check_adjacents(i,j+1)

        extra_board = [x[:] for x in board]
        for i in range(len(extra_board[0])):
            if extra_board[0][i]=='O': check_adjacents(0,i)
            if extra_board[m-1][i]=='O': check_adjacents(m-1,i)
        for i in range(1,len(extra_board)-1):
            if extra_board[i][0]=='O': check_adjacents(i,0)
            if extra_board[i][n-1]=='O': check_adjacents(i,n-1)

        for i in range(len(extra_board)):
            for j in range(len(extra_board[i])):
                if extra_board[i][j]=="O":
                    board[i][j]="X"
        return board

tests = []
solutions = []

tests.append([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
solutions.append([["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])

tests.append([["X","O","X"],["O","X","O"],["X","O","X"]])
solutions.append([["X","O","X"],["O","X","O"],["X","O","X"]])

for i in range(len(tests)):
    ans = Solution().solve(tests[i])
    print('T',i,'R',ans,solutions[i])