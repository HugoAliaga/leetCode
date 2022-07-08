class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        i=0
        while i <len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                sum = nums[i] + nums[j] + nums[k]
                if sum==0 and [nums[i],nums[j],nums[k]] not in ans:
                    ans.append([nums[i],nums[j],nums[k]])
                    while nums[k]==nums[k-1] and k>j:
                        k-=1
                    while nums[j]==nums[j+1] and k>j:
                        j+=1
                    j+=1
                    k-=1
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

tests.append([-1,0,1,2,-1,-4])
solutions.append([[-1,-1,2],[-1,0,1]])

tests.append([0,0,0,0])
solutions.append([0,0,0])

tests.append([-2,0,1,1,2])
solutions.append([[-2,0,2],[-2,1,1]])

tests.append([3,0,-2,-1,1,2])
solutions.append([[-2,-1,3],[-2,0,2],[-1,0,1]])

for i in range(len(tests)):
    result = Solution().threeSum(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])