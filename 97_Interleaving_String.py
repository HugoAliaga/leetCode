class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        def dfs(s1,s2,s3):
            if len(s1 + s2 + s3)==0:
                return True
            ans1, ans2 = False, False
            if len(s1) > 0 and len(s3) > 0 and s1[0]==s3[0]:
                ans1 = dfs(s1[1:],s2,s3[1:]) 
            if len(s2) >0 and len(s3) > 0 and s2[0]==s3[0]:
                ans2 = dfs(s1,s2[1:],s3[1:])
            return ans1 or ans2

        return dfs(s1,s2,s3)

tests = []
solutions = []

tests.append(["aabcc", "dbbca", "aadbbcbcac"])
solutions.append(True)

tests.append(["aabcc", "dbbca", "aadbbbaccc"])
solutions.append(False)

tests.append(["","",""])
solutions.append(True)

for i in range(len(tests)):
    ans = Solution().isInterleave(tests[i][0],tests[i][1],tests[i][2])
    print('T',i,'R',ans,solutions[i])