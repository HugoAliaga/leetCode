class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]

        def openClose(str,open,close):
            if open<close:
                return
            if open + close == 2*n:
                ans.append(str)
                return
            if open < n:
                openClose(str+'(',open+1,close)
            if close < n:
                openClose(str+')',open,close+1)

        openClose('',0,0)
        return ans

tests= []
solutions = []

tests.append(0)
solutions.append([''])

tests.append(1)
solutions.append(['()'])

tests.append(3)
solutions.append(["((()))","(()())","(())()","()(())","()()()"])

for i in range(len(tests)):
    result = Solution().generateParenthesis(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])