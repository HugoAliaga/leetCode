class Solution(object):
    def nextPermutation(self, nums):
        a=nums[:]
        a.sort()
        a.reverse()
        if a == nums:
            nums.sort()
            return nums
        
        r=len(nums)-1
        extra=[]
        while r>=1:
            if nums[r-1]>=nums[r]:
                extra.append(nums[r])
                r-=1
            else:
                extra.append(nums[r])
                break
        extra.sort()
        i=0
        while True:
            if extra[i]>nums[r-1]:
                temp = nums[r-1]
                nums[r-1] = extra[i]
                extra[i] = temp
                break
            else:
                i+=1
        extra.sort()
        nums[r:] = extra
        return nums

tests = []
solutions = []

tests.append([2,2,7,5,4,3,2,2,1])
solutions.append([2,2,7,5,4,3,2,2,1])
""" tests.append([1,2])
solutions.append([2,1])

tests.append([1,3,2])
solutions.append([2,1,3])

tests.append([1,2,3])
solutions.append([1,3,2])

tests.append([1,2,4,3])
solutions.append([1,3,2,4])

tests.append([5,6,7,8,7])
solutions.append([5,6,8,7,7])

tests.append([5,6,7,6,5])
solutions.append([5,7,5,6,6])

tests.append([3,2,1])
solutions.append([1,2,3])

tests.append([1,1,5])
solutions.append([1,5,1]) """

for i in range(len(tests)):
    result = Solution().nextPermutation(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])