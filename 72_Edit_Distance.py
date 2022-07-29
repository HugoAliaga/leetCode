from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        @lru_cache(maxsize=None)
        def dfs(i,j,k):
            if not i and not j:
                return k
            elif not i or not j: 
                return i or j
            elif word1[i-1]==word2[j-1]: return dfs(i-1,j-1,k)
            else:
                ans1 = 1+ dfs(i-1,j,k)  #delete
                ans2 = 1+ dfs(i-1,j-1,k) #replace
                ans3 = 1+ dfs(i,j-1,k)   #add
                return min(ans1,ans2,ans3)
        ans = 0
        ans = dfs(l1,l2,0)
        return ans

tests = []
solutions = []

tests.append(['horos','ros'])
solutions.append(2)

tests.append(['horse','ros'])
solutions.append(3)

tests.append(['intention','execution'])
solutions.append(5)

for i in range(len(tests)):
    ans = Solution().minDistance(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])