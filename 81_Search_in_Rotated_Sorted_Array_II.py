class Solution:
    def search(self, nums, target: int) -> bool:
        if not nums: return not target
        ln = len(nums)
        if len(nums)==1: return nums[0]==target
        nums.sort()
        low = 0
        high = ln-1

        while low<=high:
            mid = (high-low)//2 + low
            if target == nums[mid]:
                break
            elif nums[mid]>target:
                high = mid -1
            elif nums[mid] < target:
                low = mid+1
        if nums[mid]==target: return True
        
        return False

tests = []
solutions = []

tests.append([[2,5,6,0,0,1,2],3])
solutions.append(False)
tests.append([[1,0,1,1,1],0])
solutions.append(True)

tests.append([[5,1,3],3])
solutions.append(True)

tests.append([[2,2,2,3,2,2,2],3])
solutions.append(True)

tests.append([[],2])
solutions.append(False)

tests.append([[0],0])
solutions.append(True)

tests.append([[2],0])
solutions.append(False)

tests.append([[2],2])
solutions.append(True)

tests.append([[1,2],0])
solutions.append(False)

tests.append([[1,2],1])
solutions.append(True)

tests.append([[1,2],2])
solutions.append(True)

tests.append([[1,2],3])
solutions.append(False)

tests.append([[2,5,6,0,0,1,2],0])
solutions.append(True)

tests.append([[2,5,6,0,0,1,2],3])
solutions.append(False)

for i in range(len(tests)):
    ans = Solution().search(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])