class Solution:
    def exist(self, board, word):
        if not board: return not word
        if not word: return True
        m = len(board)
        n = len(board[0])
        def dfs(board,i,j,word):
            if len(word)==0:
                return True
            newBoard = [el[:] for el in board]
            newBoard[i][j]=0
            if i<m-1 and newBoard[i+1][j] == word[0]:
                if dfs(newBoard,i+1,j,word[1:]):
                        return True
            if i>0 and newBoard[i-1][j] == word[0]:
                if dfs(newBoard,i-1,j,word[1:]):
                        return True
            if j<n-1 and newBoard[i][j+1] == word[0]:
                if dfs(newBoard,i,j+1,word[1:]):
                        return True
            if j>0 and newBoard[i][j-1] == word[0]:
                if dfs(newBoard,i,j-1,word[1:]):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(board,i,j,word[1:]):
                        return True
        return False

tests = []
solutions = []

tests.append([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"])
solutions.append(True)

tests.append([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"])
solutions.append(True)

tests.append([[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"])
solutions.append(False)

tests.append([[["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"])
solutions.append(True)

for i in range(len(tests)):
    ans =Solution().exist(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])