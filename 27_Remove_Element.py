class Solution(object):
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=0
        items=0
        while l < len(nums):
            while nums[l]==val:
                items+=1
                if len(nums)-1-l==0:
                    nums[l]=None
                for r in range(l,len(nums)-1):
                    nums[r]=nums[r+1]
                    nums[r+1]=None
            l+=1
        return len(nums)-items

    def removeElement(self, nums, val):
        i=0
        for el in nums:
            if el != val:
                nums[i]=el
                i+=1
        return i

tests = []
solutions = []

tests.append([[3,2,2,3],3])
solutions.append([2,2,None,None])

tests.append([[0,1,2,2,3,0,4,2],2])
solutions.append([0,1,4,0,3,None,None,None])

tests.append([[0,1,1,1,1,1,1,1,1],2])
solutions.append([0,1,1,1,1,1,1,1,1])

tests.append([[0,1,1,1,1,1,1,1,1],1])
solutions.append([0])

tests.append([[1],1])
solutions.append([0])

for i in range(len(tests)):
    result = Solution().removeElement(tests[i][0],tests[i][1])
    print('Test ' + str(i),'Result',result,solutions[i])
