class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        cand_len = len(candidates)
        def dfs(cur_sum,cur_set,ans,idx):
            cur_set.sort()
            if cur_sum > target: return
            if cur_sum == target:
                if cur_set not in ans: ans.append(cur_set) 
                return
            for i in range(idx,cand_len):
                dfs(cur_sum+candidates[i],cur_set + [candidates[i]],ans,i)


        dfs(0,[],ans,0)

        return ans




tests = []
solutions = []

tests.append([[100,200,4,12],400])
solutions.append([])

tests.append([[2,3,6,7],7])
solutions.append([[2,2,3],[7]])

tests.append([[2,3,5],8])
solutions.append([[2,2,2,2],[2,3,3],[3,5]])

tests.append([[2],1])
solutions.append([])

tests.append([[48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23],69])
solutions.append([])

for i in range(len(tests)):
    result = Solution().combinationSum(tests[i][0],tests[i][1])
    print('T '+str(i),'R',result,solutions[i])