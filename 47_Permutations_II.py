#from typing import OrderedDict

class Solution(object):
    def permute(self, nums,path,res):
        ans = []
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.permute(nums[:i]+nums[i+1:],path + [nums[i]],res)

    def permuteUnique(self,nums):
        #nums = list(OrderedDict.fromkeys(nums))
        nums.sort()
        newAns = []
        """ for i in range(len(nums)):
            if nums[i] not in newNums:
                newNums.append(nums[i]) """
        res = []
        path = []
        self.permute(nums,path,res)
        for i in range(len(res)):
            if res[i] not in newAns:
                newAns.append(res[i])
        return newAns

        
tests = []
solutions = []


tests.append([1,2,2])
solutions.append([[1,2],[2,1]])

tests.append([0,1,0])
solutions.append([[0,1],[1,0]])

""" tests.append([1,1,1,1,2,3,2,3])
solutions.append([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]) """


tests.append([1])
solutions.append([1])

for i in range(len(tests)):
    result = Solution().permuteUnique(tests[i])
    print('T',i,'R',result,solutions[i])