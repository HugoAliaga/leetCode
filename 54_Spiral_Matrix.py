from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        size = height*width
        i,j = 0,0
        limit_il,limit_ir,limit_ju,limit_jd=0,width,0,height
        elements = 0

        ans = []
        while elements<size:
            while i<limit_ir:
                ans.append(matrix[j][i])
                elements+=1
                i+=1
            if elements == size: break
            i-=1
            j+=1
            while j<limit_jd:
                ans.append(matrix[j][i])
                elements+=1
                j+=1
            if elements == size: break
            j-=1
            i-=1
            while i>=limit_il:
                ans.append(matrix[j][i])
                elements+=1
                i-=1
            if elements == size: break
            i+=1
            j-=1
            while j>limit_ju:
                ans.append(matrix[j][i])
                elements+=1
                j-=1
            j+=1
            i+=1
            limit_il,limit_ir,limit_ju,limit_jd=limit_il+1,limit_ir-1,limit_ju+1,limit_jd-1
        return ans

tests = []
solutions = []

tests.append([[1,2,3],[4,5,6],[7,8,9]])
solutions.append([1,2,3,6,9,8,7,4,5])

tests.append([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
solutions.append([1,2,3,4,8,12,11,10,9,5,6,7])

for i in range(len(tests)):
    res = Solution().spiralOrder(tests[i])
    print('T',i,'R',res,solutions[i])