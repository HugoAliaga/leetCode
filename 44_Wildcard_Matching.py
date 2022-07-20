class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p and not s:
            return True

        if len(p)>len(s):
            return False
        if not s: return not p
        
        if p and s:
            if p[0]==s[0]:
                return self.isMatch(s[1:],p[1:])
            elif p[0]=='?':
                return self.isMatch(s[1:],p[1:])
            elif p[0]=='*':
                return self.isMatch(s[1:],p[1:]) or self.isMatch(s[1:],p[:]) or self.isMatch(s[:],p[1:])
        
        return False
        
tests = []
solutions = []

tests.append(["adceb","*a*b"])
solutions.append(True)

tests.append(['aa','2a'])
solutions.append(False)

tests.append(['aa','*'])
solutions.append(True)

tests.append(['cb','?a'])
solutions.append(False)


for i in range(len(tests)):
    result = Solution().isMatch(tests[i][0],tests[i][1])
    print('T',i,'R',result,solutions[i])