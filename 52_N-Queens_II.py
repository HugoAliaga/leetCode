class Solution:
    def isValid(self,n,board,x,y):
        for i in range(n):
            if board[x][i]=='Q' or board[i][y]=='Q':    #row & column
                return False
            if x-i>=0 and y-i>=0:
                if board[x-i][y-i]=='Q':
                    return False
            if x+i<n and y+i<n:
                if board[x+i][y+i]=='Q':
                    return False
            if x+i<n and y-i>=0:
                if board[x+i][y-i]=='Q':
                    return False
            if x-i>=0 and y+i<n:
                if board[x-i][y+i]=='Q':
                    return False
        return True
        
    def dfs(self,board,n,row,column,queens,boards):
        board[row][column]='Q'
        if queens == n:
            for el in range(len(board)):
                board[el]="".join(board[el])
            if board not in boards:
                boards.append(board)
            return board
        for i in range(n):
             if self.isValid(n,board,row+1,i):
                newBoard = []
                for elB in range(n):
                    newBoard.append([])
                    for elC in range(n):
                        newBoard[elB].append(board[elB][elC])
                newBoard =  self.dfs(newBoard,n,row+1,i,queens+1,boards)
                    

        
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []
        board = []
        for m in range(n):
            board.append(['.']*n)
        for i in range(n):
            board = []
            for m in range(n):
                board.append(['.']*n)
            self.dfs(board,n,0,i,1,boards)
                    
        return len(boards)



tests = []
solutions = []

tests.append(1)
solutions.append([['Q']])

tests.append(4)
solutions.append([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])

tests.append(5)
solutions.append([["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]])
tests.append(9)
solutions.append([['Q']])

for i in range(len(tests)):
    res = Solution().solveNQueens(tests[i])
    print('T',i,'R',res,solutions[i])