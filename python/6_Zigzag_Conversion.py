class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows ==1: return s
        row = 1
        goingUp = False
        working = True
        rows = []
        result = ''
        for i in range(numRows):
            rows.append('')
        for letter in s:
            rows[row-1]+=letter
            if row == numRows or goingUp:
                goingUp = True
                row -=1
                if row ==1:
                    goingUp = False
            else:
                row +=1
        for group in rows:
            result += group
        return result

tests = []
results = []

tests.append(["ABC",1])
results.append("ABC")

tests.append(["PAYPALISHIRING",3])
results.append("PAHNAPLSIIGYIR")

tests.append(["PAYPALISHIRING",4])
results.append("PINALSIGYAHRPI")

for test in range(len(tests)):
    result = Solution().convert(tests[test][0],tests[test][1])
    print('This is test ' + str(test),'Result',result,results[test])