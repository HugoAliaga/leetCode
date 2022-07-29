class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = list(a)
        num_b = list(b)
        if len(a)>len(b):
            for i in range(len(a)-len(b)):
                num_b.insert(0,"0")
        elif len(b)>len(a):
            for i in range(len(b)-len(a)):
                num_a.insert(0,"0")
        ans = []
        extra = 0
        for i,j in zip(reversed(num_a),reversed(num_b)):
            i,j = int(i),int(j)
            if j+i+extra ==3:
                ans.insert(0,"1")
                extra=1
            elif i+j+extra==2:
                ans.insert(0,"0")
                extra=1
            elif i+j+extra ==1:
                ans.insert(0,"1")
                extra=0
            else:
                ans.insert(0,"0")
                extra=0
        if extra:
            ans.insert(0,"1")
        return "".join(ans)

tests = []
solutions = []

tests.append(["11","1"])
solutions.append("100")

tests.append(["1010","1011"])
solutions.append("10101")

tests.append(["1","111"])
solutions.append("1000")


for i in range(len(tests)):
    ans = Solution().addBinary(tests[i][0],tests[i][1])
    print('T',i,'R',ans,solutions[i])