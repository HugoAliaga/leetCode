class Solution(object):
    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0,0
        op, cl = 0, 0
        maxP = 0
        while l<len(s)-1:
            if s[l] == '(':
                op = 1
                cl = 0
                r = l+1
                while r<len(s):
                    if s[r]=='(':
                        op+=1
                        r+=1
                    elif s[r]==')':
                        cl +=1
                        if op==cl:
                            if op+cl>maxP:
                                maxP=op+cl
                        elif op<cl:
                            break
                        r+=1
            l+=1
            l = max(l,)
        return maxP

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0,0
        maxP = 0
        for i in range(len(s)):
            if s[i]=='(':
                l+=1
            elif s[i] == ')':
                r+=1
            if l == r and l+r > maxP:
                maxP = l+r
            elif r>l:
                l = r = 0

        l,r=0,0        
        # traverse the string from right to left
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l+=1
            else:
                r+=1            
            if l == r:# valid balanced parantheses substring 
                maxP=max(maxP, l*2)
            elif l>r: # invalid case as '(' is more
                l=r=0
        return maxP

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest
tests = []
solutions = []

tests.append("(((((((((((((((((())(((())))()()()()()()((((")
solutions.append(24)

tests.append("(())()(()((")
solutions.append(6)

tests.append('(()')
solutions.append(2)

tests.append('')
solutions.append(0)

tests.append(')()()((()(((')
solutions.append(4)

for i in range(len(tests)):
    result = Solution().longestValidParentheses(tests[i])
    print('T'+str(i),'R:',result,solutions[i])