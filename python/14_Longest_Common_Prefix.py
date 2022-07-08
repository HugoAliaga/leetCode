class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs[0]) < 1: return ''

        ans, letter = '', ''
        match = True
        counter = 0
        while match:
            ans += letter
            if len(strs[0]) <= counter: break
            letter = strs[0][counter]
            for el in strs:
                if len(el)<= counter:
                    match = False
                    break
                if el[counter] != letter:
                    match = False
                    break
            counter += 1

        return ans

tests = []
solutions = []

tests.append(['sdljk','sdf','sdr'])
solutions.append('sd')

tests.append(['sdljk','sdf',''])
solutions.append('sd')

tests.append([])
solutions.append('')

for i in range(len(tests)):
    result = Solution().longestCommonPrefix(tests[i])
    print('Test ' + str(i), 'Result', result, solutions[i])