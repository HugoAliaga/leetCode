from collections import Counter


class Solution:
    def singleNumber(self, nums) -> int:
        nums = Counter(nums)
        for i in nums:
            if nums[i]==1:
                return i

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
            
tests = []
solutions = []

tests.append([2,2,1])
solutions.append(1)

tests.append([4,1,2,1,2])
solutions.append(4)

for i in range(len(tests)):
    ans =Solution().singleNumber2(tests[i])
    print('T',i,'R',ans,solutions[i])