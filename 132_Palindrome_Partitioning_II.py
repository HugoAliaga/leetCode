from functools import lru_cache


class Solution:

    def isPal(self,s):
        return s==s[::-1]
    def minCut2(self, s: str) -> int:
        if s==s[::-1]: return 0
        combinations = [[s]]
        cuts=0
        notFound = True
        while True:
            new_combinations = []
            while combinations:
                next_set = combinations.pop()
                found = True
                for i in range(len(next_set)):
                    elem = next_set[i]
                    if not self.isPal(elem):
                        found = False
                        for j in range(1,len(elem)):
                            if self.isPal(elem[:j]):
                                new_combinations.append([elem[j:]])
                if found: return cuts
            combinations = new_combinations[:]
            new_combinations = []
            cuts +=1
    def minCut(self, s):
        cuts = [x for x in range(-1,len(s))]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i:j]==s[j:i:-1]:
                    cuts[j+1]= min(cuts[i]+1,cuts[j+1])
        return cuts[-1]

tests = []
solutions = []

tests.append("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")
solutions.append(75)
tests.append("abba")
solutions.append(0)

tests.append("aab")
solutions.append(1)

tests.append('a')
solutions.append(0)


for i in range(len(tests)):
    ans = Solution().minCut(tests[i])
    print('T',i,'R',ans,solutions[i])