class Solution(object):
    def reverse(self, x):
        result = ''

        strNumber = str(x)
        negative = False
        if x <0:
            negative = True
            strNumber = strNumber[1:]
        for digit in strNumber:
            result = digit + result
        result = int(result)
        if negative:
            result = -result
            if result < -2**31:   return 0
            return result
        else:
            if result > 2**31 -1: return 0
            return result

tests= []
results = []

tests.append(1534236469)
results.append(0)

tests.append(123)
results.append(321)

tests.append(-123)
results.append(321)

tests.append(120)
results.append(21)

for test in range(len(tests)):
    result = Solution().reverse(tests[test])
    print('Test ' + str(test),'Result',result,results[test])