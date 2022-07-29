class Solution(object):
    def permute(self, nums):
        ans = []
        if not nums:
            return ans
        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            newNums = nums[:]
            newNums.pop(i)
            newAns = []
            newAns = self.permute(newNums)
            for j in range(len(newAns)):
                newAns[j].append(nums[i])
            ans = ans + newAns

        return ans
        
tests = []
solutions = []


tests.append([1,2])
solutions.append([[1,2],[2,1]])

tests.append([0,1])
solutions.append([[0,1],[1,0]])

tests.append([1,2,3])
solutions.append([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])


tests.append([1])
solutions.append([1])

for i in range(len(tests)):
    result = Solution().permute(tests[i])
    print('T',i,'R',result,solutions[i])