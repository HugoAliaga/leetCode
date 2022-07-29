class Solution:
    def plusOne(self, digits):
        digits[-1]+=1
        for i in range(len(digits)-2,-1,-1):
            if digits[i+1]>9:
                digits[i]+=1
                digits[i+1]-=10
            else: break
        if digits[0]>9:
            digits[0]-=10
            digits.insert(0,1)
        return digits

tests = []
solutions = []

tests.append([1,2,3])
solutions.append([1,2,4])

tests.append([1,2,9])
solutions.append([1,3,0])

tests.append([9])
solutions.append([1,0])

for i in range(len(tests)):
    ans = Solution().plusOne(tests[i])
    print('T',i,'R',ans,solutions[i])