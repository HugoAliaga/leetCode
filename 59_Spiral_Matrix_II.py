class Solution:
    def generateMatrix(self, n: int):
        
        numbers = 1
        total_numbers = n*n
        l,r,u,d = 0,0,0,0
        ans = []
        for i in range(n):
            ans.append([])
            for j in range(n):
                ans[i].append([])
        while numbers <=total_numbers:
            for i in range(l,n-r):
                if numbers > total_numbers: return ans
                ans[u][i]=numbers
                numbers+=1
            u+=1
            for i in range(u,n-d):
                if numbers > total_numbers: return ans
                ans[i][n-r-1]=numbers
                numbers+=1
            r+=1
            for i in range(n-r-1,l-1,-1):
                if numbers > total_numbers: return ans
                ans[n-d-1][i]=numbers
                numbers+=1
            d+=1
            for i in range(n-d-1,u-1,-1):
                if numbers > total_numbers: return ans
                ans[i][l]=numbers
                numbers+=1
            l+=1
        return ans

tests = []
solutions = []

tests.append(0)
solutions.append([])
tests.append(1)
solutions.append([[1]])
tests.append(2)
solutions.append([[1,2],[4,3]])
tests.append(3)
solutions.append([[1,2,3],[8,9,4],[7,6,5]])

for i in range(len(tests)):
    ans = Solution().generateMatrix(tests[i])
    print('T',i,'R',ans,solutions[i])