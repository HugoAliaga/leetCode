class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0,0
        while r<len(nums):
            if nums[l]==nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                r+=1
        l+=1

        j=l
        while l < len(nums):
            nums[l]= None
            l+=1
        return l,nums

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        for i in range(1,len(nums)):
            if nums[l]<nums[i]:
                l+=1
                nums[l]=nums[i]
        return nums

tests = []
solutions = []

tests.append([1,2,3,3,4,5,6,7,8,9])
solutions.append([1,2,3,4,5,6,7,8,9,'_'])

tests.append([1,2,3,3,4,5,6,6,7,8,9])
solutions.append([1,2,3,4,5,6,7,8,9,'_','_'])

tests.append([0,0,1,1,1,2,2,3,3,4])
solutions.append([0,1,2,3,4])

tests.append([0,0,1,1,1,1,1,1,1,1,1,1])
solutions.append([0,1])

for i in range(len(tests)):
    result = Solution().removeDuplicates2(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])