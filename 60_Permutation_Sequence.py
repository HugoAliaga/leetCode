from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        ans = []
        numbers = []
        max_perm = factorial(n)
        if k> max_perm or not n:
            return 0

        for i in range(1,n+1):
            numbers.append(i)

        def dfs(numbers,path,k,ans,objective):
            if len(numbers)==1:
                ans.append(path + str(numbers[0]))
            my_factorial = factorial(max(len(numbers)-1,0))
            for i in range(len(numbers)):
                if objective <= k+(i+1)*(my_factorial) and objective > k+(i)*(my_factorial) :
                    conc = path + str(numbers[i])
                    dfs(numbers[:i]+numbers[i+1:],conc,k+i*(my_factorial),ans,objective)
        
        dfs(numbers,'',0,ans,k)
        return ans[0]

tests = []
solutions = []

tests.append([3,4])
solutions.append("231")

tests.append([4,9])
solutions.append("2314")

tests.append([9,273815])
solutions.append("2314")

for i in range(len(tests)):
    ans = Solution().getPermutation(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])