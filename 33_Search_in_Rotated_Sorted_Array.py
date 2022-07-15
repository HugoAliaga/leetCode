class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums)==1 and target!=nums[0]:
            return -1

        l = nums[0]
        r = nums[len(nums)-1]
        if target == l:
            return 0
        if target == r:
            return len(nums)-1
        if r>l:
            if target>r or target<l:
                return -1

        if target > l:
            i = 0
            while nums[i]<target and nums[i]>=l:
                i+=1
            if nums[i]==target:
                return i

        if target < r:
            i = len(nums)-1
            while nums[i]>target and nums[i]<=r:
                i-=1
            if nums[i]==target:
                return i
        return -1

tests = []
solutions = []

tests.append([[3,5,1],5])
solutions.append(1)

tests.append([[1,3],0])
solutions.append(-1)

tests.append([[7,8,9,10,1,2],0])
solutions.append(-1)

tests.append([[4,5,6,7,0,1,2],0])
solutions.append(4)

tests.append([[4,5,6,7,0,1,2],3])
solutions.append(-1)


for i in range(len(tests)):
    result = Solution().search(tests[i][0],tests[i][1])
    print('T'+str(i),'R:',result,solutions[i])