class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        difference = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(difference)<0: return -1
        if len(difference)==1 and difference[0]==0: return 0
        ln = len(difference)
        fuel = 0
        start = 0
        for i in range(ln):
            fuel+=difference[i]
            if fuel< 0:
                start = i+1
                fuel=0

        return start

tests = []
solutions = []

tests.append([[3,1,1],[1,2,2]])
solutions.append(0)

tests.append([[5,1,2,3,4],[4,4,1,5,1]])
solutions.append(4)

tests.append([[1,2,3,4,5],[3,4,5,1,2]])
solutions.append(3)

tests.append([[2,3,4],[3,4,3]])
solutions.append(-1)

for i in range(len(tests)):
    ans = Solution().canCompleteCircuit(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])