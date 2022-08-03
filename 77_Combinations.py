class Solution:
    def combine(self, n: int, k: int):
        ans = []
        available = [i for i in range(1,n+1)]
        def dfs(path,available):
            if len(path)==k:
                ans.append(path)
            else:
                for i in range(len(available)):
                    dfs(path + [available[i]],available[i+1:])
        dfs([],available)
        return ans

tests = []
solutions = []

tests.append([4,2])
solutions.append([[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]])

tests.append([1,1])
solutions.append([[1]])

tests.append([0,0])
solutions.append([[]])

for i in range(len(tests)):
    ans = Solution().combine(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])