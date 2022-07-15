class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if target> nums[len(nums)-1]: return len(nums)
        if target< nums[0]: return 0

        l=0
        r=len(nums)-1
        
        mid = l+(r-l)//2
        item = nums[mid]
        while l<r:
            mid = l+(r-l)//2
            item = nums[mid]
            if target > item:
                l=mid+1
            elif target < item :
                r=mid
            else:
                return mid
        if target > item:
            return mid+1
        else:
            return mid

tests = []
solutions = []

tests.append([[1],1])
solutions.append(0)
tests.append([[1],2])
solutions.append(1)
tests.append([[1],0])
solutions.append(0)

tests.append([[1,3,5],1])
solutions.append(0)

tests.append([[1,2],0])
solutions.append(0)
tests.append([[1,2],1])
solutions.append(0)
tests.append([[1,2],2])
solutions.append(1)
tests.append([[1,2],3])
solutions.append(2)

tests.append([[1,3,5,6],5])
solutions.append(2)
tests.append([[1,3,5,6],2])
solutions.append(1)
tests.append([[1,3,5,6],7])
solutions.append(4)
for i in range(len(tests)):
    result = Solution().searchInsert(tests[i][0],tests[i][1])
    print('T'+str(i),'R:',result,solutions[i])