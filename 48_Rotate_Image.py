class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dimensions = len(matrix)
        savedValues = {}

        for i in range(dimensions):
            for j in range(dimensions):
                new_i, new_j = i - dimensions/2, j - dimensions/2
                new_i, new_j = int(new_j + dimensions/2), int(-new_i + dimensions/2-1)
                savedValues[(new_i,new_j)]=matrix  [new_i][new_j]
                if (i,j) in savedValues:
                    matrix[new_i][new_j]=savedValues[(i,j)]
                else:
                    matrix[new_i][new_j]=matrix[i][j]
                print(i,j,new_i,new_j)
        return matrix

tests = []
solutions = []

tests.append([[1,2,3],[4,5,6],[7,8,9]])
solutions.append([[7,4,1],[8,5,2],[9,6,3]])

tests.append([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
solutions.append([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

for i in range(len(tests)):
    result = Solution().rotate(tests[i])
    print('T',i,'R',result,solutions[i])