class Solution:
    def removeDuplicates(self, nums):
        if not nums: return []
        ln = len(nums)
        if ln==2: return nums
        l,r=0,2
        deleted = 0
        while r < ln:
            if nums[r]==nums[l]:
                deleted+=1
                nums[r]='_'
                r+=1
            elif l<r-2: 
                l+=1
            else:
                r+=1
        l,r=0,1
        while r<ln:
            if nums[r]=='_':
                r+=1
            elif nums[l]=='_':
                nums[l],nums[r]=nums[r],'_'
                l+=1
                r+=1
            else:
                l+=1
                r=l+1

        return ln-deleted

tests = []
solutions = []

tests.append([1,1,1,2,2,3])
solutions.append([1,1,2,2,3,'_'])

tests.append([0,0,1,1,1,1,2,3,3])
solutions.append([0,0,1,1,2,3,3,'_','_'])

tests.append([0,0,1,1,1,1,2,2,2,2,2,2,3,3,3])
solutions.append([0,0,1,1,2,2,3,3,'_','_','_'])

""" tests.append([1,1,1,2,2,3])
solutions.append([1,1,2,2,3,'_']) """

for i in range(len(tests)):
    ans = Solution().removeDuplicates(tests[i])
    print('T',i,'R',ans,solutions[i])