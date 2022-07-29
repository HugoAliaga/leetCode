import re


class Solution:
    def isNumber(self, s: str) -> bool:
		#Example:               +-     1 or 1. or 1.2 or .2   e or E +- 1     
        engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$")
        return engine.match(s.strip(" ")) # i prefer this over putting more things (\S*) in regex

tests = []
solutions = []

tests.append("2")
solutions.append(True)
tests.append("0089")
solutions.append(True)
tests.append("-0.1")
solutions.append(True)
tests.append("+3.14")
solutions.append(True)
tests.append("4.")
solutions.append(True)
tests.append("-.9")
solutions.append(True)
tests.append("2e10")
solutions.append(True)
tests.append("-90E3")
solutions.append(True)
tests.append("3e+7")
solutions.append(True)
tests.append("+6e-1")
solutions.append(True)
tests.append("53.5e93")
solutions.append(True)
tests.append("-123.456e789")
solutions.append(True)

tests.append("abc")
solutions.append(False)
tests.append("1a")
solutions.append(False)
tests.append("1e")
solutions.append(False)
tests.append("e3")
solutions.append(False)
tests.append("99e2.5")
solutions.append(False)
tests.append("--6")
solutions.append(False)
tests.append("-+3")
solutions.append(False)
tests.append("95a54e53")
solutions.append(False)
tests.append("95E54e53")
solutions.append(False)
tests.append(".")
solutions.append(False)
tests.append("..")
solutions.append(False)
tests.append("Re7")
solutions.append(False)



for i in range(len(tests)):
    ans = Solution().isNumber(tests[i])
    print('T',i,'R',ans,solutions[i])