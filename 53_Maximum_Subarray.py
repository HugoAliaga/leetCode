from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        memo = {}
        def dfs(i,j,max_sum,memo):
            if (i,j) in memo: return memo[(i,j)]
            max_sum = max(sum(nums[i:j]),max_sum)
            
            if i>0:
                max_sum = max(dfs(i-1,j,max_sum,memo),max_sum)
            if j<len(nums):
                max_sum = max(dfs(i,j+1,max_sum,memo),max_sum)
            """ if j-1>i:
                max_sum = max(dfs(i,j-1,max_sum,memo),max_sum)
                max_sum = max(dfs(i-1,j,max_sum,memo),max_sum) """

            memo[(i,j)] = max_sum
            return max_sum
        max_sum = -float('inf')
        for i in range(len(nums)):
            max_sum = max(dfs(i,i+1,max_sum,memo),max_sum)
        return max_sum


tests = []
solutions = []

tests.append([-2,1])
solutions.append(1)

tests.append([-2,1,-3,4,-1,2,1,-5,4])
solutions.append(6)

tests.append([1])
solutions.append(1)

tests.append([-1])
solutions.append(-1)

tests.append([5,4,-1,7,8])
solutions.append(23)

for i in range(len(tests)):
    res = Solution().maxSubArray(tests[i])
    print('T',i,'R',res,solutions[i])

