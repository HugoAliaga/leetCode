from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = -float('inf')
        max_sum = -float('inf')
        for i in range(len(nums)):
            cur_sum = max(cur_sum+nums[i],nums[i])
            max_sum = max(cur_sum,max_sum)
        return max_sum



tests = []
solutions = []

tests.append([-1,-2])
solutions.append(-1)

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

