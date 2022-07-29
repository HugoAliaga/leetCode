from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(k):
            ans = 0
            if k < n:
                ans = dfs(k+1)
            if k<n-1:
                ans +=dfs(k+2)
            if k==n:
                return 1
            return ans
        return dfs(0)


tests = []
solutions = []

tests.append(4)
solutions.append(5)

for i in range(len(tests)):
    ans = Solution().climbStairs(tests[i])
    print('T',i,'R',ans,solutions[i])