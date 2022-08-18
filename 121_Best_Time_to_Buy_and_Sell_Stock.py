class Solution:
    def maxProfit(self, prices) -> int:
        buy = prices[0]
        max_return = 0
        for i in range(len(prices)):
            buy=min(prices[i],buy)
            max_return = max(max_return,prices[i]-buy)
            
            

        return max_return


tests = []
solutions = []

tests.append([7,1,5,3,6,4])
solutions.append(5)

tests.append([7,6,4,3,1])
solutions.append(0)

for i in range(len(tests)):
    ans = Solution().maxProfit(tests[i])
    print('T',i,'R',ans,solutions[i])