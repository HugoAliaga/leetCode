class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        # SPACES
        spaces = True
        counter = 0
        while spaces:
            if s[counter] == ' ':
                counter +=1
            else :
                spaces = False
        s = s[counter:]

        #SIGN
        positive = True
        if s[0]=='-':
            positive = False
        if s[0]=='+' or s[0]=='-' :
            s = s[1:]

        #DIGITS
        digitsOn = True
        digits = '0123456789'
        counter=0
        while digitsOn and counter < len(s):
            if s[counter] in digits:
                counter +=1
            else:
                digitsOn = False
        s = s[:counter]
        if s=='':
            s=0
        if not positive:
            result = -int(s)
        else:
            result = int(s)
        if result > 2**31 - 1:
            return 2**31-1
        if result < -2**31:
            return -2**31
        return result

tests= []
solutions = []

tests.append("")
solutions.append(0)
tests.append("42")
solutions.append(42)
tests.append("   -42")
solutions.append(-42)
tests.append("4193 with words")
solutions.append(4193)

tests.append("7823438209482123432 with words")
solutions.append(2**31-1)

tests.append("words and 987")
solutions.append(0)


for test in range(len(tests)):
    result = Solution().myAtoi(tests[test])
    print('Test ' + str(test),'Result',result,solutions[test])