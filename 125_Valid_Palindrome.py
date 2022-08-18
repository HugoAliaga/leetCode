import re


class Solution:
    def isPalindrome2(self, s: str) -> bool:
        s= re.sub('[^a-zA-Z0-9]','',s)
        s= s.lower()
        while len(s)>0 and s[0]==s[-1]:
            s=s[1:-1]
        if len(s)==0 or len(s)==1: return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s= re.sub('[^a-zA-Z0-9]','',s)
        s= s.lower()
        if len(s)<2: return True

        s_reversed = s[::-1]
        if s==s_reversed:return True
        return False

tests= []
solutions = []

tests.append("0P")
solutions.append(False)

tests.append("A man, a plan, a canal: Panama")
solutions.append(True)

tests.append("race a car")
solutions.append(False)

tests.append(' ')
solutions.append(True)

for i in range(len(tests)):
    ans = Solution().isPalindrome(tests[i])
    print('T',i,'R',ans,solutions[i])