from functools import lru_cache


class Solution:
    def restoreIpAddresses(self, s: str):
        @lru_cache(maxsize=None)
        def dfs(path,idx,s):
            if s=='' and idx==4:
                ans.append(path[:-1])
                return
            if idx==4:
                return
            for i in range(1,len(s)+1):
                if int(s[:i]) < 256:
                    if len(s[:i])>1 and s[0]=='0':
                        continue
                    dfs(path+s[:i]+'.',idx+1,s[i:])
                else:
                    break
        ans = []
        dfs('',0,s)
        return ans

tests = []
solutions = []

tests.append("25525511135")
solutions.append(["255.255.11.135","255.255.111.35"])

tests.append("0000")
solutions.append(["0.0.0.0"])

tests.append("101023")
solutions.append(["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])

for i in range(len(tests)):
    ans = Solution().restoreIpAddresses(tests[i])
    print('T',i,'R',ans,solutions[i])