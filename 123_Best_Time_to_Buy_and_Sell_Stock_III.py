from ast import Delete
from functools import lru_cache
from os import remove


class Solution:
    def maxProfit3(self, prices) -> int:
        buy = 0
        stack = []
        for i in range(1,len(prices)):
            if prices[i]> prices[buy]:
                stack.append((buy,i,prices[i]-prices[buy]))
            buy = i
        i=0
        while i < len(stack)-1:
            if prices[stack[i+1][0]]==prices[stack[i][1]]:
                stack[i]=(stack[i][0],stack[i+1][1],prices[stack[i+1][1]]-prices[stack[i][0]])
                del stack[i+1]
            else: i+=1
        stack.sort(key =lambda x: x[2])
        max_return = 0 
        for i in range(min(2,len(stack))):
            max_return += stack.pop()[2]

        return max_return

    def maxProfit2(self, prices) -> int:
        @lru_cache(maxsize=None)
        def dfs(b1,s1,b2,s2):
            this_prof = prices[s1] - prices[b1] + prices[s2] - prices[b2]
            a1,a2,a3,a4 = 0,0,0,0
            if s2 < len(prices)-1: a1 = dfs(b1,s1,b2,s2+1)
            if b2 < s2: a2 = dfs(b1,s1,b2+1,s2)
            if s1 < b2: a3 = dfs(b1,s1+1,b2,s2)
            if b1 < s1: a4 = dfs(b1+1,s1,b2,s2)
            return max(this_prof,a1,a2,a3,a4)
        return dfs(0,0,0,0)

    def maxProfit(self,prices):
        ln = len(prices)-1
        @lru_cache(maxsize=None)
        def dp(price_idx,profit,actions,max_profit):
            if price_idx >ln  or not actions: return profit
            a1, a2 = 0,0
            if actions % 2 == 0:
                a1 = dp(price_idx+1,profit-prices[price_idx],actions-1)
            else:
                a1 = dp(price_idx+1,profit+prices[price_idx],actions-1)
            a2 = dp(price_idx+1,profit,actions)
            return max(a1,a2)

        return dp(0,0,4)
    def maxProfit(self, prices) -> int:
        
        n = len(prices)
        profit = [0]*n
        
        global_min = prices[0]
        for i in range(1,n):
            global_min = min(global_min,prices[i])
            profit[i] = max(profit[i-1],prices[i]-global_min)
        
        res = max(profit[-1],0)
        global_max = 0
        for i in range(n-1,0,-1):
            global_max = max(global_max,prices[i])
            res = max(res,profit[i-1]+global_max-prices[i])
        
        return res
tests = []
solutions = []

tests.append([1,2,4,2,5,7,2,4,9,0])
solutions.append(13)

tests.append([3,3,5,0,0,3,1,4])
solutions.append(6)

tests.append([1,2,3,4,5])
solutions.append(4)

tests.append([7,6,4,3,1])
solutions.append(0)

for i in range(len(tests)):
    ans = Solution().maxProfit(tests[i])
    print('T',i,'R',ans,solutions[i])