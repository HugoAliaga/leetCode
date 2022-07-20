class Solution(object):
    def solveSudoku(self, board) -> None:
        for row in range(0,9):
            for col in range(0,9):
                if(board[row][col]=="."):
                    for i in range(1,10):
                        if(self.isValid(row,col,i,board)):
                            board[row][col]=str(i)
                            solved,newSudoku = self.solveSudoku(board)
                            if(solved==True):
                                return True, newSudoku
                            else:
                                board[row][col]="."
                    return False, None
        return True, board
    def isValid(self,row,col,i,board):
        for c in range(0,9):
            if(board[row][c]==str(i)):
                return False
            if(board[c][col]==str(i)):
                return False
            if(board[3*(row//3)+(c//3)][3*(col//3)+(c%3)]==str(i)):
                return False
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        blocks = []
        columns = []
        rows = []
        for i in range(len(board)):
            columns.append([])
            blocks.append([])
            rows.append([])
        for i in range(len(board)):

            for j in range(len(board[i])):
                if board[i][j] !='.':
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    if i < 3:
                        if j <3:
                            blocks[0].append(board[i][j])
                        elif j < 6:
                            blocks[1].append(board[i][j])
                        else:
                            blocks[2].append(board[i][j])
                    elif i < 6:
                        if j <3:
                            blocks[3].append(board[i][j])
                        elif j < 6:
                            blocks[4].append(board[i][j])
                        else:
                            blocks[5].append(board[i][j])
                    else:
                        if j <3:
                            blocks[6].append(board[i][j])
                        elif j < 6:
                            blocks[7].append(board[i][j])
                        else:
                            blocks[8].append(board[i][j])
        for i in range(len(board)):
            if len(columns[i])>1:
                columns[i].sort()
                for j in range(1,len(columns[i])):
                    if columns[i][j]==columns[i][j-1]:
                        return False
            if len(rows[i])>1:
                rows[i].sort()
                for j in range(1,len(rows[i])):
                    if rows[i][j]==rows[i][j-1]:
                        return False
            if len(blocks[i])>1:
                blocks[i].sort()
                for j in range(1,len(blocks[i])):
                    if blocks[i][j]==blocks[i][j-1]:
                        return False
        return True
    
tests = []
solutions = []

tests.append([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
solutions.append(True)

tests.append([[".",".","9","7","4","8",".",".","."]
,["7",".",".",".",".",".",".",".","."]
,[".","2",".","1",".","9",".",".","."]
,[".",".","7",".",".",".","2","4","."]
,[".","6","4",".","1",".","5","9","."]
,[".","9","8",".",".",".","3",".","."]
,[".",".",".","8",".","3",".","2","."]
,[".",".",".",".",".",".",".",".","6"]
,[".",".",".","2","7","5","9",".","."]])

""" tests.append([["1","."]
,["3","."]])  """

solutions.append(False)

for i in range(len(tests)):
    result = Solution().solveSudoku(tests[i],0)
    print('T'+str(i),'R:',result,solutions[i])