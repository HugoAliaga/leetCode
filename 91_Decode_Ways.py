from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        map = {
            '1':"A","2":"B","3":"C","4":"D","5":"E","6":"F","7":"G","8":"H","9":"I","10":"J",
            "11":"K","12":"L","13":"M","14":"N","15":"O","16":"P","17":"Q","18":"R","19":"S","20":"T","21":"U","22":"V","23":"W","24":"X","25":"Y","26":"Z"
        }
        def dfs(path,s,sols):
            if s=='':
                sols.append(path)
                return
            for i in range(1,len(s)+1):
                if s[:i] in map:
                    dfs(path + map[s[:i]],s[i:],sols)
                else:
                    break
        @lru_cache(maxsize=None)
        def dfs2(s):
            if s=='':
                return 1
            sols=0
            for i in range(1,len(s)+1):
                if s[:i] in map:
                    sols += dfs2(s[i:])
                else:
                    return sols
            return sols
        sols = 0
        sols = dfs2(s)
        return sols

tests = []
solutions = []

tests.append("12")
solutions.append(2)

tests.append("226")
solutions.append(3)

tests.append("06")
solutions.append(0)

for i in range(len(tests)):
    ans = Solution().numDecodings(tests[i])
    print('T',i,'R',ans,solutions[i])