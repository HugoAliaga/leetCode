class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numCandidates = len(candidates)
        candidates.sort()
        counter = []
        maxCand = []
        ans = []
        for i in range(numCandidates):
            counter.append(0)
            maxCand.append(0)
            maxCand[i] = target // candidates[i]
        while True:
            sumCand = sum([i*j for i,j in zip(counter,candidates)])
            if sumCand == target:
                setList = []
                for i in range(numCandidates):
                    for j in range(counter[i]):
                        setList.append(candidates[i])
                if setList not in ans:
                    ans.append(setList)
            counter[0]+=1
            for i in range(numCandidates-1):
                sumCand = sum([i*j for i,j in zip(counter,candidates)])
                if counter[i]>maxCand[i] or sumCand>target:
                    counter[i]=0
                    counter[i+1]+=1
            if counter[-1]*candidates[-1]>target:
                break
            if len(ans)==150:
                break

        return ans

tests = []
solutions = []

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