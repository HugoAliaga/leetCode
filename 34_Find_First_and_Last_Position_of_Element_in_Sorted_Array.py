class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        length = len(nums)
        l=0
        r=length-1
        mid=(r+l)//2
        # Find a element == target
        while True:
            num = nums[mid]
            if target > num and l!=r:
                l = max(mid,l+1)
            elif target < num and l!=r:
                r = min(mid,r-1)
            elif target == num: # Element found
                ls, rs = mid, mid
                # See how far to stretch ls and lr
                while rs<length-1 and nums[rs+1]==target:
                    rs+=1
                while ls>0 and nums[ls-1]==target:
                    ls-=1
                return [ls,rs]
            else:
                return [-1,-1]
            mid=(r+l)//2




tests= []
solutions = []

tests.append([[1,1,2],1])
solutions.append([0,1])

tests.append([[2,2],2])
solutions.append([0,1])

tests.append([[5,7,7,8,8,10],3])
solutions.append([-1,-1])

tests.append([[5,7,7,8,8,10],8])
solutions.append([3,4])

tests.append([[],0])
solutions.append([-1,-1])

tests.append([[1],0])
solutions.append([-1,-1])

tests.append([[1],2])
solutions.append([-1,-1])

tests.append([[1],1])
solutions.append([0,0])

tests.append([[1,2],1])
solutions.append([0,0])

tests.append([[1,2],3])
solutions.append([-1,-1])

tests.append([[1,2],2])
solutions.append([1,1])

tests.append([[1,2],0])
solutions.append([-1,-1])

for i in range(len(tests)):
    result = Solution().searchRange(tests[i][0],tests[i][1])
    print('T'+str(i),'R:',result,solutions[i])