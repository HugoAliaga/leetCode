class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        steps=1
        l,r,max_r = 0, nums[0],0
        while r <n-1:
            steps+=1
            for i in range(l,r+1):
                max_r = max(max_r,i + nums[i])

            l,r=r,max_r
            if l == r:
                return False



        return True

tests = []
solutions = []

tests.append([2,3,1,1,4,2,1,3,1,2,1,1,2,1])
solutions.append(True)

tests.append([3,2,1,0,4])
solutions.append(False)

for i in range(len(tests)):
    res = Solution().canJump(tests[i])
    print('T',i,'R',res,solutions[i])