class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        l,r = 0,0
        r_max=0
        l_max=0
        rmax_vec = [0]*length
        water=0
        for r in range(length-1,0,-1):
            if height[r]>r_max:
                r_max = height[r]
            rmax_vec[r]=r_max

        for l in range(length):
            height_this = height[l]
            if height_this>l_max:
                l_max=height_this
            water += max(0,min(l_max-height_this,rmax_vec[l]-height_this))
                
        return water

tests = []
solutions = []

tests.append([1,2,3,4,5,6,7,8,9,8,7,6,5,4,2,0])
solutions.append(0)

tests.append([0,1,0,2,1,0,1,3,2,1,2,1])
solutions.append(6)

tests.append([4,2,0,3,2,5])
solutions.append(9)

for i in range(len(tests)):
    result = Solution().trap(tests[i])
    print('T',i,'R',result,solutions[i])