print('Problem starting')

class Solution(object):
    def twoSum(self, nums, target):
        for el in range(len(nums)):
            if target-nums[el] in nums:
                indexEl = nums.index(target-nums[el])
                if el != indexEl:
                    return [el,indexEl]

    def twoSum2(self, nums, target):
        seen = []
        for el in range(len(nums)):
            if target-nums[el] in seen:
                return [nums.index(target-nums[el]),el]
            else:
                seen.append(nums[el])

        

tests = []
targets =[]
solutions = []

tests.append([2,7,11,15])
targets.append(9)
solutions.append([0,1])

tests.append([3,2,4])
targets.append(6)
solutions.append([1,2])

for item in range(len(tests)):
    solution = Solution().twoSum2(tests[item],targets[item])
    print('This is run ' + str(item), solution, solutions[item])