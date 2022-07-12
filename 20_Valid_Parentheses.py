class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = ''

        for i in range(len(s)):
            if s[i] == '(':
                str += ')'
            elif s[i] == '[':
                str += ']'
            elif s[i] == '{':
                str += '}'
            elif str == '':
                return False
            elif s[i] == str[-1]:
                str = str[:-1]
            else :
                return False
        if len(str)>0:
            return False
        return True

tests = []
solutions = []

tests.append('(')
solutions.append(False)

tests.append('()')
solutions.append(True)

tests.append('[()]')
solutions.append(True)

tests.append('([]])')
solutions.append(False)

tests.append('()[]][')
solutions.append(False)

for i in range(len(tests)):
    result = Solution().isValid(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])
