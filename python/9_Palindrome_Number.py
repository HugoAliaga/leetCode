class Solution(object):
    def isPalindrome(self, x):
        strNum = str(x)
        while strNum[0]==strNum[-1]:
            strNum = strNum[1:-1]
            if len(strNum) <= 1:
                return True
        return False

    def isPalindromeNum(self, x: int) -> bool:
        orig = x
        back_x = 0
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            x = x // 10
        return orig == back_x
        
tests = []
solutions = []

tests.append(123)
solutions.append(False)

tests.append(12)
solutions.append(False)

tests.append(22)
solutions.append(True)

tests.append(12321)
solutions.append(True)

for i in range(len(tests)):
    result = Solution().isPalindromeNum(tests[i])
    print('Test '+ str(i),'Result',result,solutions[i])