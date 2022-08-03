class Solution:
    def subsets2(self, nums):
        ans = []
        def dfs(path,available):
            ans.append(path)
            for i in range(len(available)):
                dfs(path + [available[i]],available[i+1:])
        dfs([],nums)
        return ans

    def subsets(self, nums):
               #[pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        set_array = [[]]
        for i in nums:
            set_array += [pre + [i] for pre in set_array]
        return  set_array

tests = []
solutions = []

tests.append([1,2,3])
solutions.append([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])

tests.append([0])
solutions.append([[],[0]])

for i in range(len(tests)):
    ans = Solution().subsets(tests[i])
    print('T',i,'R',ans,solutions[i])