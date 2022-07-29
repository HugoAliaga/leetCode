class Solution:
    def mySqrt(self, x: int) -> int:
        upper_lim = 2**31 - 1
        lower_lim = 1
        while True:
            mid = int(0.5*upper_lim + 0.5*lower_lim)
            squared = mid*mid
            if abs((squared - x)/x)<0.00001:
                return int(mid)
            if squared >x:
                upper_lim = mid
            elif squared <x:
                lower_lim = mid+1
tests = []
solutions = []

tests.append(16)
solutions.append(4)

tests.append(625)
solutions.append(25)

tests.append(234984732)
solutions.append(1)

for i in range(len(tests)):
    ans = Solution().mySqrt(tests[i])
    print('T',i,'R',ans,solutions[i])