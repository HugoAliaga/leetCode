class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s

tests = []
results = []

for i in range(len(tests)):
    result = Solution().longestPalindrome(tests[i])
    print('Test ' + str(i),'Result',result,results[i])