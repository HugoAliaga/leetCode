class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        length = len(nums)
        if length==1:
            if nums!=[1]:
                return 1
            else: return 2
        nums.sort()
        if nums[-1]<1:
            return 1
        foundOne =False
        for i in range(1,length):
            if nums[i-1]>0:
                if nums[i-1]==1:
                    foundOne=True
                if not foundOne: return 1
                if nums[i]-nums[i-1]>1:
                    return nums[i-1]+1
            elif nums[i]>0:
                if nums[i]!=1:
                    return 1
        return nums[-1]+1
            

tests = []
solutions = []
tests.append([0,-1,3,1])
solutions.append(2)

tests.append([101,-2])
solutions.append(1)


tests.append([1,2])
solutions.append(3)

tests.append([-1,-2])
solutions.append(1)

tests.append([1,2,3,4,6,7,8,9])
solutions.append(5)

tests.append([1,2,0])
solutions.append(3)

tests.append([3,4,-1,1])
solutions.append(2)

tests.append([7,8,9,11,12])
solutions.append(1)

tests.append([1])
solutions.append(2)


for i in range(len(tests)):
    result = Solution().firstMissingPositive(tests[i])
    print('T '+str(i),'R',result,solutions[i])