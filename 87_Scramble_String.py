from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache(maxsize=None)
        def dfs(s1,s2):
            if len(s1)!=len(s2): return False
            if sorted(s1) != sorted(s2): return False
            if s1==s2 or len(s1)<4: return True

            for i in range(1,len(s1)):
                if (dfs(s1[i:],s2[i:]) and dfs(s1[:i],s2[:i])) or (dfs(s1[:i],s2[-i:]) and dfs(s1[i:],s2[:-i])):
                    return True
        
        return dfs(s1,s2)

tests = []
solutions = []
tests.append(['abc','bac'])
solutions.append(True)

tests.append(["great","rgeat"])
solutions.append(True)

tests.append(["abcde","caebd"])
solutions.append(False)

tests.append(['a','a'])
solutions.append(True)

for i in range(len(tests)):
    ans = Solution().isScramble(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])