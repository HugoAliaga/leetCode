class Solution(object):
    def romanToInt(self, s):
        map = {'M':1000 , 'D':500 , 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        num=0
        prev=99999
        for letter in s:
            if prev<map[letter]:
                num += -2*prev + map[letter]
            else:
                num += map[letter]
            prev = map[letter]
        
        return num

tests= []
solutions = []

tests.append('M')
solutions.append(1000)

solutions.append(500)
tests.append('D')

solutions.append(423)
tests.append('CDXXIII')

solutions.append(67)
tests.append('LXVII')

solutions.append(1)
tests.append('I')

solutions.append(1564)
tests.append('MDLXIV')

solutions.append(1964)
tests.append('MCMLXIV')

solutions.append(41)
tests.append('XLI')

for i in range(len(tests)):
    result = Solution().romanToInt(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])