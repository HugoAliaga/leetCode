import collections


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        candidates_count = {}
        for i in candidates:
            if i not in candidates_count:
                candidates_count[i] = 1
            else:
                candidates_count[i]+=1
        candidates_trim = []
        candidates_max = []
        for i in candidates_count:
            candidates_trim.append(i)
            candidates_max.append(candidates_count[i])
        """         candidates_count = collections.Counter(candidates)
        candidates_trim = list(candidates_count.keys())
        candidates_max = list(candidates_count.values()) """

        cand_len = len(candidates_max)

        def dfs(cur_sum,cur_set,ans,idx):
            if cur_sum > target: return
            if cur_sum == target:
                if cur_set not in ans: ans.append(cur_set) 
                return
            for i in range(idx,cand_len):
                if collections.Counter(cur_set)[candidates_trim[i]]<candidates_max[i]:
                    dfs(cur_sum+candidates_trim[i],cur_set + [candidates_trim[i]],ans,i)


        dfs(0,[],ans,0)

        return ans




tests = []
solutions = []



tests.append([[10,1,2,7,6,1,5],8])
solutions.append([[1,1,6],[1,2,5],[1,7],[2,6]])

tests.append([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27])
solutions.append([])



for i in range(len(tests)):
    result = Solution().combinationSum2(tests[i][0],tests[i][1])
    print('T '+str(i),'R',result,solutions[i])