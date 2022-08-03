class Solution:
    def subsetsWithDup(self, nums):
        ans = [[]]
        for j in nums:
            new_set = []
            for i in ans:
                if sorted(i+[j]) not in ans:
                    new_set.append(sorted(i+[j]))
            ans+=new_set
        return ans

tests = []
solutions = []

tests.append([1,2,2])
solutions.append([[],[1],[1,2],[1,2,2],[2],[2,2]])

tests.append([0])
solutions.append([])

for i in range(len(tests)):
    ans = Solution().subsetsWithDup(tests[i])
    print('T',i,'R',ans,solutions[i])