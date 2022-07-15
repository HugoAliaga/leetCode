class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        test=0
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                j=0
                while j<len(needle) and i+j < len(haystack) and haystack[i+j]==needle[j]:
                    j+=1
                if j==len(needle):
                    return i
        return -1

tests = []
solutions = []

tests.append(["hello","ll"])
solutions.append(2)

tests.append(["aaaaa","bba"])
solutions.append(-1)

tests.append(["aaa","aaaa"])
solutions.append(-1)

for i in range(len(tests)):
    result = Solution().strStr(tests[i][0],tests[i][1])
    print('Test '+str(i),'Result',result,solutions[i])