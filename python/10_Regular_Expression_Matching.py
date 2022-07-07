class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s

        firstMatch = bool(s) and p[0] in {s[0],'.'}

        if len(p)>=2 and p[1]=='*':
            return (self.isMatch(s,p[2:]) or (firstMatch and self.isMatch(s[1:],p)))
        else:
            return firstMatch and self.isMatch(s[1:],p[1:])

tests= []
solutions = []

tests.append(["aa","a"])
solutions.append(False)

tests.append(["aa","a*"])
solutions.append(True)

tests.append(["ab",".*"])
solutions.append(True)

tests.append(["ab",".*..*"])
solutions.append(True)
tests.append(["ab",".*.."])
solutions.append(True)

tests.append(["aaa","ab*a"])
solutions.append(False)
tests.append(["aaa","a*a"])
solutions.append(True)
tests.append(["ab",".*"])
solutions.append(True)
tests.append(["ab",".*c"])
solutions.append(False)
tests.append(["aaaab","c*a*b"])
solutions.append(True)
tests.append(["aab","c*a*b"])
solutions.append(True)
tests.append(["aaferefe","a.*"])
solutions.append(True)
tests.append(["aaferefe","a.b*"])
solutions.append(False)
tests.append(["aa","a*"])
solutions.append(True)

for i in range(len(tests)):
    solution = Solution().isMatch(tests[i][0],tests[i][1])
    print('Test ' + str(i),'Result',solution,solutions[i])