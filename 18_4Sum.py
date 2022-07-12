class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4: return []
        nums.sort()
        ans = []
        i=0
        while i < len(nums)-3:
            j=i+1
            k = j+1
            while j < k:
                k = j+1
                l= len(nums)-1
                while l>k:
                    sum = nums[i] + nums[j] + nums[k] + nums[l] - target
                    if sum > 0:
                        l -=1
                    elif sum < 0:
                        k +=1
                    else:
                        if [nums[i],nums[j],nums[k] ,nums[l]] not in ans: ans.append([nums[i],nums[j],nums[k] ,nums[l]])
                        k +=1
                j+=1
                while nums[j-1]==nums[j] and j<k:
                    j+=1
            i +=1
            while nums[i-1]==nums[i] and i<j:
                    i+=1
        return ans

tests = []
solutions = []

tests.append([[1,0,-1,0,-2,2],0])
solutions.append([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

tests.append([[0,0,0,0],0])
solutions.append([0,0,0,0])

for i in range(len(tests)):
    result = Solution().fourSum(tests[i][0],tests[i][1])
    print('Tests ' + str(i),'Result',result,solutions[i])