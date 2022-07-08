class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = []
        minimum = nums[0] + nums[1] + nums[2] 
        i=0
        while i <len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                sum = nums[i] + nums[j] + nums[k] - target
                if abs(sum) < abs(minimum):
                    ans = nums[i]+nums[j]+nums[k]
                    minimum = sum
                if sum==0:
                    return nums[i]+nums[j]+nums[k]
                elif sum>0 and j<k:
                    k-=1
                else:
                    j+=1

            i+=1
            while nums[i-1]==nums[i] and i<len(nums)-3:
                i+=1
        return ans        
        

tests = []
solutions = []

tests.append([[-1,2,1,-4],1])
solutions.append(2)


for i in range(len(tests)):
    result = Solution().threeSumClosest(tests[i][0],tests[i][1])
    print('Test ' + str(i),'Result',result,solutions[i])