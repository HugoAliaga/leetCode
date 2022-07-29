class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(m,n,memo):
            total = 0
            if m ==1 or n ==1:
                return 1
            if (m,n) in memo: return memo[(m,n)]
            if (n,m) in memo: return memo[(n,m)]
            
            amount= 0
            total += dfs(m,n-1,memo)
            total += dfs(m-1,n,memo)
            memo[(m,n)] = total
            return total
        memo = {}
        return dfs(m,n,memo)
tests= []
solutions = []

tests.append([1,2])
solutions.append(1)

tests.append([3,2])
solutions.append(3)

tests.append([3,7])
solutions.append(28)

tests.append([23,12])
solutions.append(2838)

for i in range(len(tests)):
    ans = Solution().uniquePaths(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])

