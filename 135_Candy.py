class Solution:
    def candy(self, ratings) -> int:
        ratings = [0]+ratings+[0]
        ln = len(ratings)
        candies = [0]+[1]*(ln-2)+[0]
        for i in range(1,ln):
            if ratings[i]>ratings[i-1]: candies[i]=candies[i-1]+1
        for i in range(ln-1,-1,-1):
            if ratings[i-1]>ratings[i]: candies[i-1]=max(candies[i-1],candies[i]+1)
        return sum(candies[1:ln-1])

tests = []
solutions = []

tests.append([1,0,2])
solutions.append(5)

tests.append([1,2,2])
solutions.append(4)

for i in range(len(tests)):
    ans = Solution().candy(tests[i])
    print('T',i,'R',ans,solutions[i])