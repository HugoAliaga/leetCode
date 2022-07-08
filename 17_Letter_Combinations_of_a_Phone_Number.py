class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        ans = []
        if not digits: return []

        for i in map[int(str(digits)[0])]:
            ans.append(i)

        for i in range(1,len(str(digits))):
            newAns = ans
            ans = []
            for j in range(len(map[int(str(digits)[i])])):
                for k in range(len(newAns)):
                    newCombo = newAns[k]+map[int(str(digits)[i])][j]
                    ans.append(newCombo)

        return ans

tests = []
solutions = []

tests.append(2)
solutions.append(['a','b','c'])

tests.append(236)
solutions.append(["ad","ae","af","bd","be","bf","cd","ce","cf"])

for i in range(len(tests)):
    result = Solution().letterCombinations(tests[i])
    print('Tests ' + str(i),'Result',result,solutions[i])