class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums: return 0
        nums.sort()
        max_cont = 1
        cont = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                cont+=1
                max_cont = max(max_cont,cont)
            elif nums[i]==nums[i-1]:
                continue
            else:
                cont=1
        return max_cont


tests = []
solutions = []

tests.append([100,4,200,1,3,2])
solutions.append(4)

tests.append([0,3,7,2,5,8,4,6,0,1])
solutions.append(9)

for i in range(len(tests)):
    ans = Solution().longestConsecutive(tests[i])
    print('T',i,'R',ans,solutions[i])