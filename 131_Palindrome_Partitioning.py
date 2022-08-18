from functools import lru_cache


class Solution:
    def partition(self, s: str):
        if not s: return []

        @lru_cache(maxsize=None)
        def isPalindrome(s):
            return s==s[::-1]

        @lru_cache(maxsize=None)
        def dfs(s):
            ans = []
            if not s: return
            if isPalindrome(s):
                ans.append([s])
            ans1=[]
            ans2=[]
            for i in range(1,len(s)):
                if isPalindrome(s[:i]):
                    second_part = dfs(s[i:])
                    for j in second_part:
                        ans.append([s[:i]]+j)                            
            return ans
        return dfs(s)

tests = []
solutions = []

tests.append("abba")
solutions.append([["a","a","b"],["aa","b"]])

tests.append("aab")
solutions.append([["a","a","b"],["aa","b"]])

tests.append('a')
solutions.append([['a']])


for i in range(len(tests)):
    ans = Solution().partition(tests[i])
    print('T',i,'R',ans,solutions[i])