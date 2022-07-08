class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea,l,r = 0,0, len(height)-1
        while l<r:
            if height[l]>height[r]:
                tempArea = height[r]*(r-l)
                r-=1
            else:
                tempArea = height[l]*(r-l)
                l+=1
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea

tests = []
solutions = []

tests.append([1,1])
solutions.append(1)

tests.append([1,8,6,2,5,4,8,3,7])
solutions.append(49)

for i in range(len(tests)):
    result = Solution().maxArea(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])