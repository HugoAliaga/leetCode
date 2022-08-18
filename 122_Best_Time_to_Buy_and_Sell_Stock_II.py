class Solution:
    def maxProfit(self, prices) -> int:
        buy = 0
        max_return = 0
        for i in range(1,len(prices)):
            if prices[i]> prices[buy]:
                max_return +=prices[i]-prices[buy]
            buy = i
            
        return max_return


tests = []
solutions = []

tests.append([7,1,5,3,6,4])
solutions.append(7)

tests.append([1,2,3,4,5])
solutions.append(4)

for i in range(len(tests)):
    ans = Solution().maxProfit(tests[i])
    print('T',i,'R',ans,solutions[i])