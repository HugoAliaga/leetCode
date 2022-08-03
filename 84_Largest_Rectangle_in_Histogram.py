from urllib.parse import MAX_CACHE_SIZE


class Solution:
    def largestRectangleAreaSlow(self, heights) -> int:
        height_length = {}
        max_rect = 0
        for i in range(len(heights)):
            for j in range(1,heights[i]+1):
                if j not in height_length:
                    height_length[j] = 0
            for j in height_length:
                if j <= heights[i]:
                    height_length[j]+=1
                else:
                    max_rect = max(max_rect,int(j)*height_length[j])
                    height_length[j]=0
        for i in height_length:
            max_rect = max(max_rect,int(i)*height_length[i])

        return max_rect

    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

tests = []
solutions = []

tests.append([2,1,5,6,2,3])
solutions.append(10)

tests.append([2,4])
solutions.append(4)

for i in range(len(tests)):
    ans = Solution().largestRectangleArea(tests[i])
    print('T',i,'R',ans,solutions[i])