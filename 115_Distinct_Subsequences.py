from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def numDistinct(self, s: str, t: str) -> int:
        if not t and s: return 1
        if len(t)>len(s): return 0
        if t==s: return 1
        if len(t)==len(s): return 0
        ans=0
        ans+=self.numDistinct(s[1:],t)
        if s[0]==t[0]:
            ans+=self.numDistinct(s[1:],t[1:])
        return ans

tests= []
solutions = []

tests.append(["rabbbit","rabbit"])
solutions.append(3)

tests.append(["babgbag","bag"])
solutions.append(5)

for i in range(len(tests)):
    ans = Solution().numDistinct(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])