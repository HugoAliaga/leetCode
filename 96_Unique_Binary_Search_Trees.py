from functools import lru_cache


class Solution:       
    def numTrees(self,n):

        @lru_cache(maxsize=None)
        def dfs(n):
            if n == 1 or n == 0 : return 1
            if n ==2: return 2
            if n == 3: return 5
            ans = 0
            for i in range(0,n):
                ans+= dfs(i)*dfs(n-i-1)
            return ans
        return dfs(n)

tests = []
solutions = []

tests.append(2)
solutions.append(1)

tests.append(1)
solutions.append(1)

tests.append(3)
solutions.append(5)

tests.append(4)
solutions.append(14)

for i in range(len(tests)):
    ans = Solution().numTrees(tests[i])
    print('T',i,'R',ans,solutions[i])