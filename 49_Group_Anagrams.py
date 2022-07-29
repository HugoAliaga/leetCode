class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        res = []
        for i in range(len(strs)):
            check = "".join(sorted(strs[i]))

            if check not in groups:
                groups[check]=[strs[i]]
            else:
                groups[check].append(strs[i])
        
        return groups.values()

tests = []
solutions = []

tests.append(["eat","tea","tan","ate","nat","bat"])
solutions.append([["bat"],["nat","tan"],["ate","eat","tea"]])

tests.append([""])
solutions.append([[""]])

tests.append(["a"])
solutions.append([["a"]])

for i in range(len(tests)):
    res = Solution().groupAnagrams(tests[i])
    print('T',i,'R',res,solutions[i])