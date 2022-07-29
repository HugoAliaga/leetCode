class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        i=0
        while i< len(matrix)-1:
            if target>matrix[i][-1]:
                i+=1
            else: break
        if len(matrix[i])==1:
            if matrix[i][0]==target: return True
        low=0
        high =len(matrix[i])-1
        while high>low:
            mid = int((high-low)/2 + low)
            if target > matrix[i][mid]:
                low=mid+1
            elif target < matrix[i][mid]:
                high = mid-1
            else:
                return True
        if target == matrix[i][high] or target == matrix[i][low]:
            return True
        return False

tests = []
solutions = []
tests.append([[[1]],1])
solutions.append(True)

tests.append([[[]],1])
solutions.append(False)

tests.append([[[1,2]],1])
solutions.append(True)
tests.append([[[1,2]],2])
solutions.append(True)
tests.append([[[1,2]],3])
solutions.append(False)
tests.append([[[1,2]],0])
solutions.append(False)

tests.append([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],16])
solutions.append(True)

tests.append([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],21])
solutions.append(False)

tests.append([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],3])
solutions.append(True)

tests.append([[[1,3,5,7],[10,11,16,20],[23,30,34,60]],13])
solutions.append(False)

for i in range(len(tests)):
    ans = Solution().searchMatrix(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])
