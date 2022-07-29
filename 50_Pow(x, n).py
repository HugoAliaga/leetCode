class Solution(object):
    def myPow(self, x, n):
        if n == 0 :
            return 1
        if n < 0:
            n = -n
            x = 1/x

        if n%2==0:
            res=x
            while n>1:
                newRes = res
                res = res*x
                if res==newRes: return res
                n-=1
        else:
            if x>0:
                res=x
                while n>1:
                    newRes = res
                    res = res*x
                    if res==newRes: return res
                    n-=1
            else:
                x=abs(x)
                res=x
                while n>1:
                    newRes = res
                    res = res*x
                    if res==newRes: return -res
                    n-=1

                return -res
        return res

tests = []
solutions = []

tests.append([1,2])
solutions.append(1**2)

tests.append([2.0000,10])
solutions.append(1024)

tests.append([2.1,3])
solutions.append(9.26100)

tests.append([2,-2])
solutions.append(2**(-2))

tests.append([0.00001,2147483647])
solutions.append(0.00001**2147483647)

tests.append([-1,-2147483647])
solutions.append(-1.00000**-2147483647)

for i in range(len(tests)):
    res = Solution().myPow(tests[i][0],tests[i][1])
    print('T',i,'R',res,solutions[i])