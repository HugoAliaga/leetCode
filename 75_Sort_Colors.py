class Solution:
    def sortColors(self, nums):
        stack0=0
        stack1=0
        stack2=0
        for i in nums:
            if i==0:
                stack0 +=1
            elif i==1:
                stack1 +=1
            else:
                stack2 +=1
        i=0
        while stack0>0:
            nums[i]=0
            stack0-=1
            i+=1
        while stack1>0:
            nums[i]=1
            stack1-=1
            i+=1
        while stack2>0:
            nums[i]=2
            stack2-=1
            i+=1
        return nums

    def sortColors2(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return nums

tests = []
solutions = []

tests.append([2,0,2,1,1,0])
solutions.append([0,0,1,1,2,2])

tests.append([2,0,1])
solutions.append([0,1,2])

tests.append([])
solutions.append([])

tests.append([1,1,1,1,1])
solutions.append([1,1,1,1,1])

tests.append([2,2,2,2,2,2,1,1,1,1,2])
solutions.append([1,1,1,1,2,2,2,2,2,2,2])

tests.append([0,1,2,1,0,2,1,2,1,2,0,2,0,2,1,0,1,0,1,2,1,2,0,1,2,1,0,2])
solutions.append([0,1,2,1,0,2,1,2,1,2,0,2,0,2,1,0,1,0,1,2,1,2,0,1,2,1,0,2].sort())

for i in range(len(tests)):
    ans = Solution().sortColors2(tests[i])
    print('T',i,'R',ans,solutions[i])